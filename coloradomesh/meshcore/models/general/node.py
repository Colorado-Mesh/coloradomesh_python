from typing import Optional

from coloradomesh.internal import BaseModel
from coloradomesh.internal.utils import timestamp_within_delta
from coloradomesh.meshcore.models.general.node_status import NodeStatus
from coloradomesh.meshcore.models.general.node_type import NodeType
from coloradomesh.meshcore.utils import build_meshcore_contact_url


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
    is_observer: bool = False

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
        return build_meshcore_contact_url(name=self.name, public_key=self._public_key_cleaned)

    def to_hash(self) -> int:
        """
        Generate a hash value for this node
        :return: An integer hash value representing this node.
        """
        _input = f"{self.name}:{self._public_key_cleaned}:{self.node_type.value}:{self.latitude}:{self.longitude}:{self.is_observer}"
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
            'is_observer': self.is_observer,
            'status': self.status.value,
            'contact': self.contact_url,
        }
