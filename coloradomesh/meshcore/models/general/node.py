from typing import Optional

from coloradomesh.internal import BaseModel
from coloradomesh.internal.utils import timestamp_within_delta
from coloradomesh.meshcore.models.general.node_params import NodeParams
from coloradomesh.meshcore.models.general.node_status import NodeStatus
from coloradomesh.meshcore.models.general.node_type import NodeType
from coloradomesh.meshcore.models.general.region import Regions
from coloradomesh.meshcore.models.general.repeater_name import RepeaterName
from coloradomesh.meshcore.utils import build_meshcore_contact_url


class _FollowsNamingScheme:
    """
    Abstract base class for all node types that should adhere to the naming schema.
    """

    def __init__(self, node: Node):
        self._node = node
        self._name_segments: Optional[RepeaterName] = None

    @property
    def name_segments(self) -> Optional[RepeaterName]:
        """
        Parses the node name into the naming schema.
        :return: A RepeaterName object representing the segments of the node name, or None if the name does not follow the naming schema.
        """
        if not self._name_segments:
            try:
                # This process isn't intense parsing (e.g. regex), but we'll cache the result still
                self._name_segments = RepeaterName.from_name_string(name_string=self._node.name)
            except ValueError:
                pass

        return self._name_segments

    @property
    def name_adheres_to_schema(self) -> bool:
        """
        Returns whether the name adheres to the naming schema.
        :return: A boolean representing whether the name adheres to the naming schema.
        """
        return self.name_segments is not None  # Would be None if could not parse (invalid)


class _SpecificNodeType(BaseModel):
    """
    Abstract base class for all specific node types.
    """

    def __init__(self, node: Node):
        super().__init__()
        self._node = node

    @property
    def name(self) -> str:
        return self._node.name


class Node(BaseModel):
    """
    Represents a MeshCore node on the ColoradoMesh network.
    """
    public_key: str
    name: str
    node_type: NodeType
    created_at: int  # Unix timestamp
    last_heard: int  # Unix timestamp
    owner: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    params: Optional[NodeParams] = None
    estimated_region_iata: Optional[str] = None

    @property
    def _public_key_cleaned(self) -> str:
        """
        Return the formatted public key.
        This ensures that the public key is in a consistent format for extracting the ID and comparing with other nodes.
        :return: The cleaned public key.
        :rtype: str
        """
        return self.public_key.upper()

    @property
    def public_key_id(self) -> str:
        """
        Return the first two bytes (4-character hex string) of the public key, which is used as an identifier for the node.
        Always returns the public key ID in uppercase to ensure consistency when comparing with other nodes.
        :return: The first two bytes of the public key as a hex string, in uppercase.
        :rtype: str
        """
        return self.public_key_id_4_char

    @property
    def public_key_id_4_char(self) -> str:
        """
        Return the first two bytes (4-character hex string) of the public key, which is used as an identifier for the node.
        Always returns the public key ID in uppercase to ensure consistency when comparing with other nodes.
        :return: The first two bytes of the public key as a hex string, in uppercase.
        :rtype: str
        """
        return self._public_key_cleaned[:4]

    @property
    def public_key_id_2_char(self) -> str:
        """
        Return the first byte (2-character hex string) of the public key, which is used as an identifier for the node.
        Always returns the public key ID in uppercase to ensure consistency when comparing with other nodes.
        :return: The first byte of the public key as a hex string, in uppercase.
        :rtype: str
        """
        return self._public_key_cleaned[:2]

    @property
    def public_key_id_first_char(self) -> str:
        """
        Return the first character (1-character hex string) of the public key, which is used as an identifier for the node.
        Always returns the public key ID in uppercase to ensure consistency when comparing with other nodes.
        :return: The first character of the public key as a hex string, in uppercase.
        :rtype: str
        """
        return self._public_key_cleaned[0]

    @property
    def public_key_id_second_char(self) -> str:
        """
        Return the second character (1-character hex string) of the public key, which is used as an identifier for the node.
        Always returns the public key ID in uppercase to ensure consistency when comparing with other nodes.
        :return: The second character of the public key as a hex string, in uppercase.
        :rtype: str
        """
        return self._public_key_cleaned[1]

    @property
    def public_key_id_third_char(self) -> str:
        """
        Return the third character (1-character hex string) of the public key, which is used as an identifier for the node.
        Always returns the public key ID in uppercase to ensure consistency when comparing with other nodes.
        :return: The third character of the public key as a hex string, in uppercase.
        :rtype: str
        """
        return self._public_key_cleaned[2]

    @property
    def public_key_id_fourth_char(self) -> str:
        """
        Return the fourth character (1-character hex string) of the public key, which is used as an identifier for the node.
        Always returns the public key ID in uppercase to ensure consistency when comparing with other nodes.
        :return: The fourth character of the public key as a hex string, in uppercase.
        :rtype: str
        """
        return self._public_key_cleaned[3]

    @property
    def status(self) -> NodeStatus:
        """
        Determine the status of this node based on its created_at and last_heard timestamps.
        :return: A NodeStatus value representing the status of this node.
        """
        if not self.last_heard:  # Not sure when last heard, so we can't determine status
            return NodeStatus.UNKNOWN
        elif timestamp_within_delta(timestamp=self.created_at, days=2):  # First heard within the last 2 days
            return NodeStatus.NEW
        elif timestamp_within_delta(timestamp=self.last_heard, days=7):  # Last heard within the last 7 days
            return NodeStatus.ACTIVE
        else:  # Last heard was more than 7 days ago
            return NodeStatus.STALE

    @property
    def contact_url(self) -> str:
        """
        Return the MeshCore contact URL for this node.
        :return: The contact URL for this node.
        :rtype: str
        """
        return build_meshcore_contact_url(name=self.name,
                                          public_key=self._public_key_cleaned,
                                          node_type=self.node_type.value)

    @property
    def estimated_region(self) -> Optional[Regions]:
        """
        Return the estimated region of this node.
        :return: A Region object representing the estimated region of this node, or None if it cannot be determined.
        :rtype: Regions
        """
        return Regions.from_code(code=self.estimated_region_iata) if self.estimated_region_iata else None

    @property
    def is_repeater(self) -> bool:
        """
        Return whether this node is a repeater.
        :return: A boolean value representing whether this node is a repeater.
        """
        return self.node_type == NodeType.REPEATER

    @property
    def is_room_server(self) -> bool:
        """
        Return whether this node is a room server.
        :return: A boolean value representing whether this node is a room server.
        """
        return self.node_type == NodeType.ROOM_SERVER

    @property
    def is_companion(self) -> bool:
        """
        Return whether this node is a companion.
        :return: A boolean value representing whether this node is a companion.
        """
        return self.node_type == NodeType.COMPANION

    @property
    def is_sensor(self) -> bool:
        """
        Return whether this node is a sensor.
        :return: A boolean value representing whether this node is a sensor.
        """
        return self.node_type == NodeType.SENSOR

    def to_hash(self) -> int:
        """
        Generate a hash value for this node
        :return: An integer hash value representing this node.
        """
        _input = f"{self.name}:{self._public_key_cleaned}:{self.node_type.value}:{self.latitude}:{self.longitude}:{self.params}"
        return hash(_input)

    def to_json(self) -> dict:
        """
        Serialize this node to a JSON-compatible dictionary
        :return: A dictionary representation of this node that can be serialized to JSON.
        """
        return {
            'id': self.public_key_id,
            'public_key': self.public_key,
            'name': self.name,
            'node_type': self.node_type.value,
            'created_at': self.created_at,
            'last_heard': self.last_heard,
            'owner': self.owner,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'status': self.status.value,
            'contact': self.contact_url,
            'params': self.params.to_json() if self.params else {},
            'estimated_region_iata': self.estimated_region_iata,
        }
