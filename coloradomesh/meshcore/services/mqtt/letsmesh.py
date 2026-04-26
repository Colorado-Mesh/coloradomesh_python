import logging
from datetime import datetime
from typing import Callable, Optional, Any

import paho.mqtt.client as mqtt

from coloradomesh.meshcore.services.mqtt._base import (
    MQTTBroker,
    TokenBasedMQTTBrokerAuth,
    get_logger,
    random_seed
)


class LetsMeshMQTTBroker(MQTTBroker):
    def __init__(
            self,
            client_name: str,
            public_key: str,
            private_key_hex: str,
            on_connect_callback: Optional[Callable[[Any, Any, int], None]] = None,
            on_disconnect_callback: Optional[Callable[[Any, int], None]] = None,
            on_message_callback: Optional[Callable[[Any, mqtt.MQTTMessage], None]] = None,
            heartbeat_callback: Optional[Callable[[datetime], None]] = None,
            heartbeat_interval: int = 60,
            logger: Optional[logging.Logger] = None,
    ):
        logger = logger or get_logger(name=client_name)
        super().__init__(
            client_name=client_name,
            broker_name="LetsMesh",
            broker_host="mqtt-us-v1.letsmesh.net",
            broker_port=443,
            use_tls=True,
            use_websockets=True,
            auth=TokenBasedMQTTBrokerAuth(
                public_key=public_key,
                private_key_hex=private_key_hex,
                audience="mqtt-us-v1.letsmesh.net",
                jwt_expiry_minutes=10,
                seed=random_seed(),
                logger=logger
            ),
            on_connect_callback=on_connect_callback,
            on_disconnect_callback=on_disconnect_callback,
            on_message_callback=on_message_callback,
            heartbeat_callback=heartbeat_callback,
            heartbeat_interval=heartbeat_interval,
            logger=logger
        )
