from typing import Optional

from coloradomesh.internal import BaseModel
from coloradomesh.meshtastic.models.general.node_role import NodeRole


class Node(BaseModel):
    """
    Represents a Meshtastic node on the Colorado Mesh network.
    """
    id: int
    long_name: str
    short_name: str
    role: NodeRole
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None
    precision: Optional[int] = None
    hardware_model: Optional[str] = None

    def to_hash(self) -> int:
        """
        Generate a hash value for this node
        :return: An integer hash value representing this node.
        """
        _input = f"{self.id}:{self.long_name}:{self.short_name}:{self.role.value}:{self.latitude}:{self.longitude}:{self.altitude}:{self.precision}:{self.hardware_model}"
        return hash(_input)

    def to_json(self) -> dict:
        """
        Serialize this node to a JSON-compatible dictionary
        :return: A dictionary representation of this node that can be serialized to JSON.
        """
        return {
            'id': self.id,
            'long_name': self.long_name,
            'short_name': self.short_name,
            'role': self.role.value,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'altitude': self.altitude,
            'precision': self.precision,
            'hardware_model': self.hardware_model
        }
