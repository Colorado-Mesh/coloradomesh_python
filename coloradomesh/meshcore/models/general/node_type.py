import enum


class NodeType(enum.Enum):
    """
    Enum representing the type of MeshCore node on the ColoradoMesh network.
    """
    UNKNOWN = 0
    COMPANION = 1
    REPEATER = 2
    ROOM_SERVER = 3
    SENSOR = 4

    @classmethod
    def from_int(cls, role: int) -> 'NodeType':
        if role == 1:
            return cls.REPEATER
        elif role == 2:
            return cls.ROOM_SERVER
        elif role == 3:
            return cls.COMPANION
        elif role == 4:
            return cls.SENSOR
        elif role == 0:
            return cls.UNKNOWN
        else:
            raise ValueError(f"Unknown device role: {role}")
