from coloradomesh.meshcore.models.general.node import Node, _SpecificNodeType, _FollowsNamingScheme
from coloradomesh.meshcore.models.general.node_type import NodeType


class Repeater(_SpecificNodeType, _FollowsNamingScheme):
    """
    Represents a MeshCore repeater (or room server) on the ColoradoMesh network.
    """

    def __init__(self, node: Node):
        _SpecificNodeType.__init__(self, node=node)
        _FollowsNamingScheme.__init__(self, node=node)

    @classmethod
    def from_node(cls, node: Node) -> 'Repeater':
        if node.node_type is not NodeType.REPEATER:
            raise ValueError(f"Node with ID {node.public_key_id} is not a repeater")
        return Repeater(node=node)
