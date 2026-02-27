import enum

from denvermesh.meshcore.models.general.node_type import NodeType


class NodeRole(enum.Enum):
    """
    Enum representing the device role of a MeshCore node via the LetsMesh API.
    """
    COMPANION = 1
    REPEATER = 2
    ROOM = 3

    @classmethod
    def from_int(cls, role: int) -> 'NodeRole':
        if role == 1:
            return cls.COMPANION
        elif role == 2:
            return cls.REPEATER
        elif role == 3:
            return cls.ROOM
        else:
            raise ValueError(f"Unknown device role: {role}")

    @property
    def to_node_type(self) -> NodeType:
        """
        Convert this LetsMesh NodeRole to the corresponding DenverMesh MeshCore NodeType.
        :return:
        """
        if self == NodeRole.COMPANION:
            return NodeType.COMPANION
        elif self == NodeRole.REPEATER:
            return NodeType.REPEATER
        elif self == NodeRole.ROOM:
            return NodeType.ROOM_SERVER
        else:
            raise ValueError(f"Unknown device role: {self.value}")
