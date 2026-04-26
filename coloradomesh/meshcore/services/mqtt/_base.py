import binascii
import hashlib
import json
import logging
import os
import ssl
import threading
import time
from base64 import urlsafe_b64encode as b64encode
from datetime import datetime, timedelta, UTC
from typing import Callable, Optional, Any

import paho.mqtt.client as mqtt
from nacl.bindings import (
    crypto_core_ed25519_scalar_add,
    crypto_core_ed25519_scalar_mul,
    crypto_core_ed25519_scalar_reduce,
    crypto_scalarmult_ed25519_base_noclamp,
)
from nacl.signing import SigningKey


def b64url(b: bytes):
    return b64encode(b).decode("UTF-8").rstrip("=")


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(f"mqtt.broker.{name}")


def random_seed() -> str:
    return os.urandom(32).hex()


class MQTTBrokerAuth:
    def __init__(
            self,
            logger: Optional[logging.Logger] = None,
    ):
        self._logger = logger

    def add_auth(self, client: mqtt.Client) -> mqtt.Client:
        raise NotImplementedError()

    def refresh_auth(self, client: mqtt.Client) -> mqtt.Client:
        raise NotImplementedError()

    def auth_expired(self, connection_start_time: datetime) -> bool:
        raise NotImplementedError()

    def log_debug(self, message: str):
        if self._logger:
            self._logger.debug(message)


class PasswordBasedMQTTBrokerAuth(MQTTBrokerAuth):
    def __init__(
            self,
            username: str,
            password: str,
            logger: Optional[logging.Logger] = None,
    ):
        self._username = username
        self._password = password
        super().__init__(logger=logger)

    def add_auth(self, client: mqtt.Client) -> mqtt.Client:
        client.username_pw_set(username=self._username, password=self._password)

        return client

    def refresh_auth(self, client: mqtt.Client) -> mqtt.Client:
        client.username_pw_set(username=self._username, password=self._password)

        return client

    def auth_expired(self, connection_start_time: datetime) -> bool:
        return False


class TokenBasedMQTTBrokerAuth(MQTTBrokerAuth):
    def __init__(
            self,
            public_key: str,
            private_key_hex: str,
            audience: str,
            jwt_expiry_minutes: int,
            seed: str,
            logger: Optional[logging.Logger] = None,
    ):
        self._public_key = public_key
        self._private_key_hex = private_key_hex
        self._audience = audience
        self._jwt_expiry_minutes = jwt_expiry_minutes
        self._seed = seed
        super().__init__(logger=logger)

    def _sign(
            self,
            message_hex: str,
            private_key_hex: str,
            public_key_hex: str
    ) -> bytes:
        message_bytes = binascii.unhexlify(message_hex)
        private_key_bytes = binascii.unhexlify(private_key_hex)
        public_key_bytes = binascii.unhexlify(public_key_hex)

        if len(public_key_bytes) != 32:
            raise ValueError(
                f"Invalid public key length: expected 32 bytes, got {len(public_key_bytes)}"
            )

        if len(private_key_bytes) == 32:
            # Support standard Ed25519 seed-based private keys as well.
            signing_key = SigningKey(private_key_bytes)
            derived_public_key = signing_key.verify_key.encode()
            if derived_public_key != public_key_bytes:
                raise ValueError("Provided private key does not match provided public key")
            return signing_key.sign(message_bytes).signature

        if len(private_key_bytes) != 64:
            raise ValueError(
                f"Invalid private key length: expected 32 or 64 bytes, got {len(private_key_bytes)}"
            )

        # MeshCore uses ORLP expanded Ed25519 private keys: a || prefix (both 32 bytes).
        expanded_scalar = private_key_bytes[:32]
        nonce_prefix = private_key_bytes[32:]

        derived_public_key = crypto_scalarmult_ed25519_base_noclamp(expanded_scalar)
        if derived_public_key != public_key_bytes:
            raise ValueError("Provided private key does not match provided public key")

        # Ed25519 signing with ExpandedSecretKey semantics (compatible with ORLP format).
        r_digest = hashlib.sha512(nonce_prefix + message_bytes).digest()
        r_scalar = crypto_core_ed25519_scalar_reduce(r_digest)
        r_encoded = crypto_scalarmult_ed25519_base_noclamp(r_scalar)

        k_digest = hashlib.sha512(r_encoded + public_key_bytes + message_bytes).digest()
        k_scalar = crypto_core_ed25519_scalar_reduce(k_digest)

        ka_scalar = crypto_core_ed25519_scalar_mul(k_scalar, expanded_scalar)
        s_scalar = crypto_core_ed25519_scalar_add(r_scalar, ka_scalar)

        signature_bytes = r_encoded + s_scalar

        return signature_bytes

    def _generate_jwt(self) -> str:
        now = datetime.now(tz=UTC)
        headers = {"alg": "Ed25519", "typ": "JWT"}

        payload = {
            "publicKey": self._public_key.upper(),
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(minutes=self._jwt_expiry_minutes)).timestamp()),
            "aud": self._audience,
        }

        header_b64 = b64url(json.dumps(headers, separators=(",", ":")).encode("utf-8"))
        payload_b64 = b64url(json.dumps(payload, separators=(",", ":")).encode("utf-8"))

        signing_input = f"{header_b64}.{payload_b64}"
        signing_input_bytes = signing_input.encode("utf-8")
        signing_input_hex = binascii.hexlify(signing_input_bytes).decode("utf-8")

        signature_bytes = self._sign(signing_input_hex, self._private_key_hex, payload["publicKey"])
        signature_hex = binascii.hexlify(signature_bytes).decode("utf-8").upper()

        token = f"{header_b64}.{payload_b64}.{signature_hex}"
        self.log_debug(f"Generated MeshCore token: {token[:10]}...{token[-10:]}")

        return token

    def add_auth(self, client: mqtt.Client) -> mqtt.Client:
        token = self._generate_jwt()
        username = f"v1_{self._public_key}"
        client.username_pw_set(username=username, password=token)

        return client

    def refresh_auth(self, client: mqtt.Client) -> mqtt.Client:
        return self.add_auth(client=client)

    def auth_expired(self, connection_start_time: datetime) -> bool:
        elapsed = (datetime.now(UTC) - connection_start_time).total_seconds()
        expiry_seconds = self._jwt_expiry_minutes * 60
        return elapsed >= expiry_seconds * 0.8


class MQTTBroker:
    def __init__(
            self,
            client_name: str,  # Should be your public key
            broker_name: str,
            broker_host: str,
            broker_port: int,
            use_tls: bool,
            use_websockets: bool,
            auth: MQTTBrokerAuth,
            on_connect_callback: Optional[Callable[[Any, Any, int], None]] = None,
            on_disconnect_callback: Optional[Callable[[Any, int], None]] = None,
            on_message_callback: Optional[Callable[[Any, mqtt.MQTTMessage], None]] = None,
            heartbeat_callback: Optional[Callable[[datetime], None]] = None,
            heartbeat_interval: int = 60,
            logger: Optional[logging.Logger] = None,
    ):
        self.client_name = client_name
        self.broker_name = broker_name
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.use_tls = use_tls
        self.use_websockets = use_websockets
        self._auth = auth
        self._on_connect_callback = on_connect_callback
        self._on_disconnect_callback = on_disconnect_callback
        self._on_message_callback = on_message_callback
        self._heartbeat_callback = heartbeat_callback
        self._heartbeat_interval = heartbeat_interval
        self._logger = logger or get_logger(name=client_name)

        self._connection_start_time = None
        self._running: bool = False
        self._reauth_task = None
        self._heartbeat_task = None

        self._client: mqtt.Client = None  # type: ignore

    def _prepare_client(self) -> mqtt.Client:
        client = mqtt.Client(
            client_id=self.client_name,
            transport="websockets" if self.use_websockets else "tcp",
        )

        if self.use_tls:
            # Enable TLS with certificate verification
            client.tls_set(
                cert_reqs=ssl.CERT_REQUIRED,
                tls_version=ssl.PROTOCOL_TLS_CLIENT
            )
            client.tls_insecure_set(False)  # Enforce hostname verification

        # Add auth
        client = self._auth.add_auth(client=client)

        # Register callbacks
        client.on_connect = self._on_connect
        client.on_disconnect = self._on_disconnect
        client.on_message = self._on_message

        return client

    def _connection_expired(self) -> bool:
        return self._auth.auth_expired(connection_start_time=self._connection_start_time)

    def _refresh_auth(self):
        self._client = self._auth.refresh_auth(client=self._client)
        self._connection_start_time = datetime.now(UTC)

    def _handle_auth_refresh(self):
        """Background thread that handles auth refresh"""
        while self._running:
            if self._auth.auth_expired(connection_start_time=self._connection_start_time):
                self._logger.info("Auth expired, refreshing credentials...")
                try:
                    self._refresh_auth()
                except Exception as e:
                    self._logger.error(f"Failed to refresh auth, disconnecting: {e}")
                    self._client.disconnect()

                time.sleep(60)  # Check auth every 60 seconds

    def _on_connect(self, client: mqtt.Client, userdata: Any, flags: dict[str, Any], reason_code: int):
        if reason_code != 0:
            self._logger.error(f"Failed to connect to MQTT broker {self.broker_name} with code {reason_code}")
            return

        self._logger.info(f"Client {self.client_name} connected to MQTT broker {self.broker_name}")
        self._running = True

        self._reauth_task = threading.Thread(target=self._handle_auth_refresh, daemon=True)
        self._reauth_task.start()

        if self._heartbeat_callback:
            self._heartbeat_task = threading.Thread(target=self._heartbeat, daemon=True)
            self._heartbeat_task.start()

        if self._on_connect_callback:
            self._on_connect_callback(userdata, flags, reason_code)

    def _on_disconnect(self, client: mqtt.Client, userdata: Any, reason_code: int):
        self._running = False
        self._reauth_task.stop()
        if self._heartbeat_callback:
            self._heartbeat_task.stop()

        if self._on_disconnect_callback:
            self._on_disconnect_callback(userdata, reason_code)

    def _on_message(self, client: mqtt.Client, userdata: Any, msg: mqtt.MQTTMessage):
        if self._on_message_callback:
            self._on_message_callback(userdata, msg)

    def _heartbeat(self):
        """Background thread that publishes periodic status updates"""
        while self._running:
            # We know the callback exists at this point
            self._heartbeat_callback(self._connection_start_time)

            time.sleep(self._heartbeat_interval)

    def connect(self):
        self._client = self._prepare_client()
        self._connection_start_time = datetime.now(UTC)

        self._client.connect(host=self.broker_host, port=self.broker_port, keepalive=60)

        self._client.loop_start()

    def connect_forever(self):
        self._client = self._prepare_client()
        self._connection_start_time = datetime.now(UTC)

        self._client.connect(host=self.broker_host, port=self.broker_port, keepalive=60)

        self._client.loop_forever()

    def disconnect(self):
        if self._client:
            self._client.loop_stop()
            self._client.disconnect()
            self._client = None  # type: ignore
