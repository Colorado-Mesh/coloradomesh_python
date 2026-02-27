import enum


class RepeaterType(enum.Enum):
    """
    Enum representing the type of MeshCore repeater/room server node on the DenverMesh network.
    """
    REPEATER_CORE = "Repeater - Core"
    REPEATER_DISTRIBUTOR = "Repeater - Distributor"
    REPEATER_EDGE = "Repeater - Edge"
    REPEATER_MOBILE = "Repeater - Mobile"
    ROOM_SERVER_STANDARD = "Room Server - Standard"
    ROOM_SERVER_MOBILE = "Room Server - Mobile"
    ROOM_SERVER_REPEAT_ENABLED = "Room Server - Repeat Enabled"

    @classmethod
    def to_acronym(cls, node_type: 'RepeaterType') -> str:
        """
        Convert a RepeaterType to its corresponding acronym.
        :param node_type: The RepeaterType to convert.
        :type node_type: RepeaterType
        :return: The corresponding acronym (the first letter of the type).
        :rtype: str
        """
        if node_type == cls.REPEATER_CORE:
            return "RC"
        elif node_type == cls.REPEATER_DISTRIBUTOR:
            return "RD"
        elif node_type == cls.REPEATER_EDGE:
            return "RE"
        elif node_type == cls.REPEATER_MOBILE:
            return "RM"
        elif node_type == cls.ROOM_SERVER_STANDARD:
            return "TS"
        elif node_type == cls.ROOM_SERVER_REPEAT_ENABLED:
            return "TR"
        elif node_type == cls.ROOM_SERVER_MOBILE:
            return "TM"
        else:
            raise ValueError(f"Unknown node type: {node_type}")
