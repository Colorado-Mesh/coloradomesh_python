from coloradomesh.meshcore.models.general.node import Node, _SpecificNodeType, _FollowsNamingScheme
from coloradomesh.meshcore.models.general.node_type import NodeType


class RoomServer(_SpecificNodeType, _FollowsNamingScheme):
    """
    Represents a MeshCore room server on the Colorado Mesh network.
    """

    def __init__(self, node: Node):
        _SpecificNodeType.__init__(self, node=node)
        _FollowsNamingScheme.__init__(self, node=node)

    @classmethod
    def from_node(cls, node: Node) -> 'RoomServer':
        if node.node_type is not NodeType.ROOM_SERVER:
            raise ValueError(f"Node with ID {node.public_key_id} is not a room server.")
        return RoomServer(node=node)
