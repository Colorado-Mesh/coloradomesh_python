import binascii
import json
import string
import subprocess
from base64 import urlsafe_b64decode

import pytest
from nacl.signing import VerifyKey

from coloradomesh.meshcore.services.mqtt._base import TokenBasedMQTTBrokerAuth
from coloradomesh.meshcore.services.public_keys import _generate_orlp_ed25519_keypair_bytes


def _to_hex(value: bytes) -> str:
    return binascii.hexlify(value).decode("utf-8").upper()


def _b64url_decode(value: str) -> bytes:
    padding = "=" * ((4 - (len(value) % 4)) % 4)
    return urlsafe_b64decode(value + padding)


def _decode_signature_segment(value: str) -> bytes:
    # meshcore-decoder emits uppercase hex for JWT signatures.
    if len(value) == 128 and all(c in string.hexdigits for c in value):
        return binascii.unhexlify(value)
    return _b64url_decode(value)


def _meshcore_decoder_token(public_key_hex: str, private_key_hex: str, ttl_seconds: int, audience: str) -> str:
    claims = json.dumps({"aud": audience})
    result: subprocess.CompletedProcess[str] | None = None
    try:
        result = subprocess.run(
            [
                "meshcore-decoder",
                "auth-token",
                public_key_hex,
                private_key_hex,
                "-e",
                str(ttl_seconds),
                "-c",
                claims,
            ],
            capture_output=True,
            text=True,
            timeout=10,
        )
    except FileNotFoundError:
        pytest.skip("meshcore-decoder is not installed")

    if result is None:
        pytest.skip("meshcore-decoder execution did not produce output")

    if result.returncode != 0:
        pytest.skip(f"meshcore-decoder auth-token failed: {result.stderr.strip()}")

    token = result.stdout.strip()
    if token.count(".") != 2:
        pytest.skip("meshcore-decoder returned an invalid token format")

    return token


def test_generate_jwt_signature_verifies_with_public_key_from_payload():
    public_key_bytes, private_key_bytes = _generate_orlp_ed25519_keypair_bytes()
    public_key_hex = _to_hex(public_key_bytes)

    auth = TokenBasedMQTTBrokerAuth(
        public_key=public_key_hex,
        private_key_hex=_to_hex(private_key_bytes),
        audience="mqtt.example.org",
        jwt_expiry_minutes=10,
        seed="unused",
    )

    token = auth._generate_jwt()
    header_b64, payload_b64, signature_b64 = token.split(".")

    payload = json.loads(_b64url_decode(payload_b64).decode("utf-8"))
    assert payload["publicKey"] == public_key_hex

    signing_input = f"{header_b64}.{payload_b64}".encode("utf-8")
    signature = _decode_signature_segment(signature_b64)

    VerifyKey(public_key_bytes).verify(signing_input, signature)


def test_sign_raises_when_private_key_and_public_key_do_not_match():
    public_key_bytes, private_key_bytes = _generate_orlp_ed25519_keypair_bytes()
    other_public_key_bytes, _ = _generate_orlp_ed25519_keypair_bytes()

    auth = TokenBasedMQTTBrokerAuth(
        public_key=_to_hex(public_key_bytes),
        private_key_hex=_to_hex(private_key_bytes),
        audience="mqtt.example.org",
        jwt_expiry_minutes=10,
        seed="unused",
    )

    with pytest.raises(ValueError, match="does not match"):
        auth._sign(
            message_hex=binascii.hexlify(b"hello-world").decode("utf-8"),
            private_key_hex=_to_hex(private_key_bytes),
            public_key_hex=_to_hex(other_public_key_bytes),
        )


def test_generate_jwt_interoperates_with_meshcore_decoder_token_format():
    public_key_bytes, private_key_bytes = _generate_orlp_ed25519_keypair_bytes()
    public_key_hex = _to_hex(public_key_bytes)
    private_key_hex = _to_hex(private_key_bytes)
    audience = "mqtt.example.org"

    auth = TokenBasedMQTTBrokerAuth(
        public_key=public_key_hex,
        private_key_hex=private_key_hex,
        audience=audience,
        jwt_expiry_minutes=10,
        seed="unused",
    )

    our_token = auth._generate_jwt()
    decoder_token = _meshcore_decoder_token(
        public_key_hex=public_key_hex,
        private_key_hex=private_key_hex,
        ttl_seconds=600,
        audience=audience,
    )

    our_header_b64, our_payload_b64, our_sig_segment = our_token.split(".")
    decoder_header_b64, decoder_payload_b64, decoder_sig_segment = decoder_token.split(".")

    assert all(c in string.hexdigits for c in our_sig_segment)
    assert all(c in string.hexdigits for c in decoder_sig_segment)
    assert len(our_sig_segment) == len(decoder_sig_segment) == 128

    our_payload = json.loads(_b64url_decode(our_payload_b64).decode("utf-8"))
    decoder_payload = json.loads(_b64url_decode(decoder_payload_b64).decode("utf-8"))
    assert set(our_payload) == set(decoder_payload) == {"publicKey", "iat", "exp", "aud"}
    assert our_payload["publicKey"] == decoder_payload["publicKey"] == public_key_hex
    assert our_payload["aud"] == decoder_payload["aud"] == audience

    our_signature = _decode_signature_segment(our_sig_segment)
    decoder_signature = _decode_signature_segment(decoder_sig_segment)
    VerifyKey(public_key_bytes).verify(f"{our_header_b64}.{our_payload_b64}".encode("utf-8"), our_signature)
    VerifyKey(public_key_bytes).verify(
        f"{decoder_header_b64}.{decoder_payload_b64}".encode("utf-8"),
        decoder_signature,
    )


