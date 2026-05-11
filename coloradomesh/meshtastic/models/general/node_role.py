import enum


class NodeRole(enum.Enum):
    """
    Enum representing the role of Meshtastic node on the Colorado Mesh network.
    """
    UNKNOWN = -1
    CLIENT = 0
    CLIENT_MUTE = 1
    ROUTER = 2
    ROUTER_CLIENT = 3
    REPEATER = 4
    TRACKER = 5
    SENSOR = 6
    TAK = 7
    CLIENT_HIDDEN = 8
    LOST_AND_FOUND = 9
    TAK_TRACKER = 10
    ROUTER_LATE = 11
    CLIENT_BASE = 12

    @classmethod
    def from_int(cls, role: int) -> 'NodeRole':
        if role == -1:
            return cls.UNKNOWN
        if role == 0:
            return cls.CLIENT
        if role == 1:
            return cls.CLIENT_MUTE
        elif role == 2:
            return cls.ROUTER
        elif role == 3:
            return cls.ROUTER_CLIENT
        elif role == 4:
            return cls.REPEATER
        elif role == 5:
            return cls.TRACKER
        elif role == 6:
            return cls.SENSOR
        elif role == 7:
            return cls.TAK
        elif role == 8:
            return cls.CLIENT_HIDDEN
        elif role == 9:
            return cls.LOST_AND_FOUND
        elif role == 10:
            return cls.TAK_TRACKER
        elif role == 11:
            return cls.ROUTER_LATE
        elif role == 12:
            return cls.CLIENT_BASE
        else:
            raise ValueError(f"Unknown device role: {role}")

    @classmethod
    def from_name(cls, name: str) -> 'NodeRole':
        if name == "UNKNOWN":
            return cls.UNKNOWN
        if name == "CLIENT":
            return cls.CLIENT
        if name == "CLIENT_MUTE":
            return cls.CLIENT_MUTE
        if name == "ROUTER":
            return cls.ROUTER
        if name == "ROUTER_CLIENT":
            return cls.ROUTER_CLIENT
        if name == "REPEATER":
            return cls.REPEATER
        if name == "TRACKER":
            return cls.TRACKER
        if name == "SENSOR":
            return cls.SENSOR
        if name == "TAK":
            return cls.TAK
        if name == "CLIENT_HIDDEN":
            return cls.CLIENT_HIDDEN
        if name == "LOST_AND_FOUND":
            return cls.LOST_AND_FOUND
        if name == "TAK_TRACKER":
            return cls.TAK_TRACKER
        if name == "ROUTER_LATE":
            return cls.ROUTER_LATE
        if name == "CLIENT_BASE":
            return cls.CLIENT_BASE
        else:
            raise ValueError(f"Unknown device role: {name}")
