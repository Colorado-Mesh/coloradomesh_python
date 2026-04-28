from coloradomesh.meshcore.models.general.node import Node, _SpecificNodeType
from coloradomesh.meshcore.models.general.node_type import NodeType


class Companion(_SpecificNodeType):
    """
    Represents a MeshCore companion on the Colorado Mesh network.
    """

    def __init__(self, node: Node):
        _SpecificNodeType.__init__(self, node=node)

    @classmethod
    def from_node(cls, node: Node) -> 'Companion':
        if node.node_type is not NodeType.COMPANION:
            raise ValueError(f"Node with ID {node.public_key_id} is not a companion.")
        return Companion(node=node)
