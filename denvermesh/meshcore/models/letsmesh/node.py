from typing import Optional

from denvermesh.internal import BaseModel
from denvermesh.meshcore.models.letsmesh.node_role import NodeRole


class NodeLocation(BaseModel):
    """
    Represents the location of a MeshCore node as returned by the LetsMesh API.
    """
    latitude: float
    longitude: float


class LetsMeshNode(BaseModel):
    """
    Represents a MeshCore node as returned by the LetsMesh API.
    """
    public_key: str
    name: str
    device_role: NodeRole
    regions: list[str]
    first_seen: str  # ISO 8601 timestamp
    last_seen: str  # ISO 8601 timestamp
    is_mqtt_connected: bool
    location: Optional[NodeLocation] = None
