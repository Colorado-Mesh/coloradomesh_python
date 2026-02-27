import enum

from denvermesh.meshcore.models.general.repeater_settings import RepeaterSettings
from denvermesh.meshcore.standards import (
    REPEATER_SETTINGS_HILLTOP,
    REPEATER_SETTINGS_FOOTHILLS,
    REPEATER_SETTINGS_LOCAL,
    REPEATER_SETTINGS_MOBILE,
    REPEATER_SETTINGS_SUBURBAN,
    DEFAULT_REPEATER_SETTINGS
)


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

    @classmethod
    def from_name(cls, name: str) -> 'RepeaterType':
        """
        Convert a string name to a RepeaterType enum member.
        :param name: The name of the RepeaterType (e.g. "REPEATER_CORE").
        :type name: str
        :return: The corresponding RepeaterType enum member.
        :rtype: RepeaterType
        """
        name = name.upper()
        if name in ["CORE", "REPEATER_CORE", "RC"]:
            return cls.REPEATER_CORE
        elif name in ["DISTRIBUTOR", "REPEATER_DISTRIBUTOR", "RD"]:
            return cls.REPEATER_DISTRIBUTOR
        elif name in ["EDGE", "REPEATER_EDGE", "RE"]:
            return cls.REPEATER_EDGE
        elif name in ["MOBILE", "REPEATER_MOBILE", "RM"]:
            return cls.REPEATER_MOBILE
        elif name in ["ROOM_STANDARD", "ROOM_SERVER_STANDARD", "TS"]:
            return cls.ROOM_SERVER_STANDARD
        elif name in ["ROOM_MOBILE", "ROOM_SERVER_MOBILE", "TM"]:
            return cls.ROOM_SERVER_MOBILE
        elif name in ["ROOM_REPEAT_ENABLED", "ROOM_SERVER_REPEAT_ENABLED", "TR"]:
            return cls.ROOM_SERVER_REPEAT_ENABLED
        else:
            raise ValueError(f"Unknown RepeaterType name: {name}")

    @property
    def recommended_settings(self) -> RepeaterSettings:
        """
        Get the recommended RepeaterSettings for this RepeaterType.
        :return: The recommended RepeaterSettings for this RepeaterType.
        :rtype: RepeaterSettings
        """
        if self == RepeaterType.REPEATER_CORE:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **REPEATER_SETTINGS_HILLTOP})
        elif self == RepeaterType.REPEATER_DISTRIBUTOR:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **REPEATER_SETTINGS_FOOTHILLS})
        elif self == RepeaterType.REPEATER_EDGE:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **REPEATER_SETTINGS_LOCAL})
        elif self == RepeaterType.REPEATER_MOBILE:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **REPEATER_SETTINGS_MOBILE})
        elif self == RepeaterType.ROOM_SERVER_STANDARD:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **REPEATER_SETTINGS_LOCAL})
        elif self == RepeaterType.ROOM_SERVER_REPEAT_ENABLED:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **REPEATER_SETTINGS_SUBURBAN})
        elif self == RepeaterType.ROOM_SERVER_MOBILE:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **REPEATER_SETTINGS_MOBILE})
        else:
            raise ValueError(f"Unknown node type: {self.value}")
