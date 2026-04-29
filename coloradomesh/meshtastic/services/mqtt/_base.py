import logging
from datetime import datetime, UTC
from typing import Callable, Optional

from meshtastic_mqtt_json import MeshtasticMQTT


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(f"mqtt.broker.{name}")


class MeshtasticMQTTMessage:
    def __init__(self,
                 data: dict,
                 ):
        self._data = data
        self._decoded_payload = data.get("decoded", {}).get("payload", {})

    @property
    def payload(self) -> dict:
        return self._decoded_payload


class MQTTBroker:
    def __init__(self,
                 client_name: str,
                 broker_name: str,
                 broker_host: str,
                 broker_port: int,
                 root: str,
                 username: str,
                 password: str,
                 channel: str,
                 key: str,
                 on_admin_message_callback: Optional[Callable[MeshtasticMQTTMessage]] = None,
                 on_atak_forwarder_message_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_atak_plugin_message_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_audio_message_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_detection_sensor_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_ip_tunnel_message_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_neighbor_info_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_node_info_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_people_count_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_position_callback: Callable[[MeshtasticMQTTMessage], None] = None,
                 on_private_message_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_range_test_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_remote_hardware_control_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_reply_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_routing_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_serial_communication_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_simulator_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_store_and_forward_message_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_telemetry_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_text_message_callback: Callable[[MeshtasticMQTTMessage], None] = None,
                 on_compressed_text_message_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_traceroute_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_waypoint_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 on_zone_position_system_callback: Optional[Callable[[MeshtasticMQTTMessage], None]] = None,
                 logger: Optional[logging.Logger] = None,
                 ):
        """
        :param client_name: User client name
        :param broker_name: MQTT broker name
        :param broker_host: MQTT broker host
        :param broker_port: MQTT broker port
        :param root: Root topic for MQTT broker
        :param username: MQTT username
        :param password: MQTT password
        :param channel: MQTT channel (combined with root)
        :param key: Channel key for decryption
        :param on_admin_message_callback: Callback for admin messages
        :param on_atak_forwarder_message_callback: Callback for ATAK forwarder messages
        :param on_atak_plugin_message_callback: Callback for ATAK plugin messages
        :param on_audio_message_callback: Callback for audio messages
        :param on_detection_sensor_callback: Callback for detection sensor data
        :param on_ip_tunnel_message_callback: Callback for IP tunneling messages
        :param on_neighbor_info_callback: Callback for neighbor info
        :param on_node_info_callback: Callback for node info and details
        :param on_people_count_callback: Callback for people counter
        :param on_position_callback: Callback for GPS position updates
        :param on_private_message_callback: Callback for private messages
        :param on_range_test_callback: Callback for range testing data
        :param on_remote_hardware_control_callback: Callback for remote hardware control
        :param on_reply_callback: Callback for reply message
        :param on_routing_callback: Callback for routing information
        :param on_serial_communication_callback: Callback for serial communication
        :param on_simulator_callback: Callback for simulator messages
        :param on_store_and_forward_message_callback: Callback for store and forward messages
        :param on_telemetry_callback: Callback for device telemetry data
        :param on_text_message_callback: Callback for plain text messages
        :param on_compressed_text_message_callback: Callback for compressed text messages
        :param on_traceroute_callback: Callback for network route tracing
        :param on_waypoint_callback: Callback for waypoint information
        :param on_zone_position_system_callback: Callback for zone position system messages
        :param logger: Optional logger
        """
        self.client_name = client_name
        self.broker_name: str = broker_name
        self.broker_host: str = broker_host
        self.broker_port: int = broker_port
        self.root: str = root
        self.channel: str = channel
        self._username: str = username
        self._password: str = password
        self._key: str = key

        self._on_admin_message_callback = on_admin_message_callback
        self._on_atak_forwarder_message_callback = on_atak_forwarder_message_callback
        self._on_atak_plugin_message_callback = on_atak_plugin_message_callback
        self._on_audio_message_callback = on_audio_message_callback
        self._on_detection_sensor_callback = on_detection_sensor_callback
        self._on_ip_tunnel_message_callback = on_ip_tunnel_message_callback
        self._on_neighbor_info_callback = on_neighbor_info_callback
        self._on_node_info_callback = on_node_info_callback
        self._on_people_count_callback = on_people_count_callback
        self._on_position_callback = on_position_callback
        self._on_private_message_callback = on_private_message_callback
        self._on_range_test_callback = on_range_test_callback
        self._on_remote_hardware_control_callback = on_remote_hardware_control_callback
        self._on_reply_callback = on_reply_callback
        self._on_routing_callback = on_routing_callback
        self._on_serial_communication_callback = on_serial_communication_callback
        self._on_simulator_callback = on_simulator_callback
        self._on_store_and_forward_message_callback = on_store_and_forward_message_callback
        self._on_telemetry_callback = on_telemetry_callback
        self._on_text_message_callback = on_text_message_callback
        self._on_compressed_text_message_callback = on_compressed_text_message_callback
        self._on_traceroute_callback = on_traceroute_callback
        self._on_waypoint_callback = on_waypoint_callback
        self._on_zone_position_system_callback = on_zone_position_system_callback

        self._logger = logger or get_logger(name=client_name)

        self._connection_start_time = None
        self._running: bool = False
        self._reauth_task = None
        self._heartbeat_task = None

        self._client: MeshtasticMQTT = None

    def _prepare_client(self) -> MeshtasticMQTT:
        client = MeshtasticMQTT()

        client.register_callback('ADMIN_APP', self._on_admin_message)
        client.register_callback('ATAK_FORWARDER', self._on_atak_forwarder_message)
        client.register_callback('ATAK_PLUGIN', self._on_atak_plugin_message)
        client.register_callback('AUDIO_APP', self._on_audio_message)
        client.register_callback('DETECTION_SENSOR_APP', self._on_detection_sensor)
        client.register_callback('IP_TUNNEL_APP', self._on_ip_tunnel_message)
        client.register_callback('NEIGHBORINFO_APP', self._on_neighbor_info)
        client.register_callback('NODEINFO_APP', self._on_node_info)
        client.register_callback('PAXCOUNTER_APP', self._on_people_count)
        client.register_callback('POSITION_APP', self._on_position)
        client.register_callback('PRIVATE_APP', self._on_private_message)
        client.register_callback('RANGE_TEST_APP', self._on_range_test)
        client.register_callback('REMOTE_HARDWARE_APP', self._on_remote_hardware_control)
        client.register_callback('REPLY_APP', self._on_reply)
        client.register_callback('ROUTING_APP', self._on_routing)
        client.register_callback('SERIAL_APP', self._on_serial_communication)
        client.register_callback('SIMULATOR_APP', self._on_simulator)
        client.register_callback('STORE_FORWARD_APP', self._on_store_and_forward_message)
        client.register_callback('TELEMETRY_APP', self._on_telemetry)
        client.register_callback('TEXT_MESSAGE_APP', self._on_text_message)
        client.register_callback('TEXT_MESSAGE_COMPRESSED_APP', self._on_compressed_text_message)
        client.register_callback('TRACEROUTE_APP', self._on_traceroute)
        client.register_callback('WAYPOINT_APP', self._on_waypoint)
        client.register_callback('ZPS_APP', self._on_zone_position_system)

        return client

    def _on_admin_message(self, json_data):
        if self._on_admin_message_callback:
            self._on_admin_message_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_atak_forwarder_message(self, json_data):
        if self._on_atak_forwarder_message_callback:
            self._on_atak_forwarder_message_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_atak_plugin_message(self, json_data):
        if self._on_atak_plugin_message_callback:
            self._on_atak_plugin_message_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_audio_message(self, json_data):
        if self._on_audio_message_callback:
            self._on_audio_message_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_detection_sensor(self, json_data):
        if self._on_detection_sensor_callback:
            self._on_detection_sensor_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_ip_tunnel_message(self, json_data):
        if self._on_ip_tunnel_message_callback:
            self._on_ip_tunnel_message_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_neighbor_info(self, json_data):
        if self._on_neighbor_info_callback:
            self._on_neighbor_info_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_node_info(self, json_data):
        if self._on_node_info_callback:
            self._on_node_info_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_people_count(self, json_data):
        if self._on_people_count_callback:
            self._on_people_count_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_position(self, json_data):
        if self._on_position_callback:
            self._on_position_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_private_message(self, json_data):
        if self._on_private_message_callback:
            self._on_private_message_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_range_test(self, json_data):
        if self._on_range_test_callback:
            self._on_range_test_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_remote_hardware_control(self, json_data):
        if self._on_remote_hardware_control_callback:
            self._on_remote_hardware_control_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_reply(self, json_data):
        if self._on_reply_callback:
            self._on_reply_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_routing(self, json_data):
        if self._on_routing_callback:
            self._on_routing_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_serial_communication(self, json_data):
        if self._on_serial_communication_callback:
            self._on_serial_communication_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_simulator(self, json_data):
        if self._on_simulator_callback:
            self._on_simulator_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_store_and_forward_message(self, json_data):
        if self._on_store_and_forward_message_callback:
            self._on_store_and_forward_message_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_telemetry(self, json_data):
        if self._on_telemetry_callback:
            self._on_telemetry_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_text_message(self, json_data):
        if self._on_text_message_callback:
            self._on_text_message_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_compressed_text_message(self, json_data):
        if self._on_compressed_text_message_callback:
            self._on_compressed_text_message_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_traceroute(self, json_data):
        if self._on_traceroute_callback:
            self._on_traceroute_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_waypoint(self, json_data):
        if self._on_waypoint_callback:
            self._on_waypoint_callback(MeshtasticMQTTMessage(data=json_data))

    def _on_zone_position_system(self, json_data):
        if self._on_zone_position_system_callback:
            self._on_zone_position_system_callback(MeshtasticMQTTMessage(data=json_data))

    def connect_forever(self):
        self._client = self._prepare_client()
        self._connection_start_time = datetime.now(UTC)

        self._client.connect(
            broker=self.broker_host,
            port=self.broker_port,
            root=self.root,
            channel=self.channel,
            username=self._username,
            password=self._password,
            key=self._key
        )

    def disconnect(self):
        if self._client:
            del self._client
