import enum

from coloradomesh.meshcore.models.general.repeater_settings import RepeaterSettings
from coloradomesh.meshcore.standards import (
    REPEATER_SETTINGS_HILLTOP,
    REPEATER_SETTINGS_FOOTHILLS,
    REPEATER_SETTINGS_LOCAL,
    REPEATER_SETTINGS_MOBILE,
    REPEATER_SETTINGS_SUBURBAN,
    DEFAULT_REPEATER_SETTINGS
)


class RepeaterType(int, enum.Enum):
    """
    Enum representing the type of MeshCore repeater/room server node on the ColoradoMesh network.
    """
    REPEATER_CORE = 1, "Repeater - Core", "RC", ["CORE", "REPEATER_CORE"]
    REPEATER_DISTRIBUTOR = 2, "Repeater - Distributor", "RD", ["DISTRIBUTOR", "REPEATER_DISTRIBUTOR"]
    REPEATER_EDGE = 3, "Repeater - Edge", "RE", ["EDGE", "REPEATER_EDGE"]
    REPEATER_MOBILE = 4, "Repeater - Mobile", "RM", ["MOBILE", "REPEATER_MOBILE"]
    ROOM_SERVER_STANDARD = 5, "Room Server - Standard", "TS", ["ROOM_STANDARD", "ROOM_SERVER_STANDARD"]
    ROOM_SERVER_MOBILE = 6, "Room Server - Mobile", "TM", ["ROOM_MOBILE", "ROOM_SERVER_MOBILE"]
    ROOM_SERVER_REPEAT_ENABLED = 7, "Room Server - Repeat Enabled", "TR", ["ROOM_REPEAT_ENABLED",
                                                                           "ROOM_SERVER_REPEAT_ENABLED"]

    def __new__(
            cls,
            value_int: int,
            value_str: str,
            abbreviation: str,
            keywords: list[str],
    ) -> RepeaterType:
        obj = int.__new__(cls, value_int)
        obj._value_ = value_int

        obj.human_readable = value_str
        obj.abbreviation = abbreviation
        obj.keywords = keywords

        return obj  # type: ignore

    @classmethod
    def to_acronym(cls, node_type: 'RepeaterType') -> str:
        """
        Convert a RepeaterType to its corresponding acronym.
        :param node_type: The RepeaterType to convert.
        :type node_type: RepeaterType
        :return: The corresponding acronym (the first letter of the type).
        :rtype: str
        """
        return node_type.abbreviation

    @classmethod
    def from_int(cls, value: int) -> 'RepeaterType':
        """
        Convert an integer value to a RepeaterType enum member.
        :param value: The integer value of the RepeaterType (e.g. 1 for REPEATER_CORE).
        :type value: int
        :return: The corresponding RepeaterType enum member.
        :rtype: RepeaterType
        """
        for _enum in cls:
            if _enum.value == value:
                return _enum

        raise ValueError(f"Unknown node type value: {value}")

    @classmethod
    def from_text(cls, name: str) -> 'RepeaterType':
        """
        Convert a string name to a RepeaterType enum member.
        :param name: The name of the RepeaterType (e.g. "REPEATER_CORE").
        :type name: str
        :return: The corresponding RepeaterType enum member.
        :rtype: RepeaterType
        """
        name = name.upper()
        for _enum in cls:
            terms = [_enum.human_readable] + _enum.keywords + [_enum.abbreviation.upper()]
            if name in terms:
                return _enum

        raise ValueError(f"Unknown RepeaterType name: {name}")

    @property
    def recommended_settings(self) -> RepeaterSettings:
        """
        Get the recommended RepeaterSettings for this RepeaterType.
        :return: The recommended RepeaterSettings for this RepeaterType.
        :rtype: RepeaterSettings
        """
        repeater_type = {
            'repeater_type': self.value
        }
        if self == RepeaterType.REPEATER_CORE:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **repeater_type, **REPEATER_SETTINGS_HILLTOP})
        elif self == RepeaterType.REPEATER_DISTRIBUTOR:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **repeater_type, **REPEATER_SETTINGS_FOOTHILLS})
        elif self == RepeaterType.REPEATER_EDGE:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **repeater_type, **REPEATER_SETTINGS_LOCAL})
        elif self == RepeaterType.REPEATER_MOBILE:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **repeater_type, **REPEATER_SETTINGS_MOBILE})
        elif self == RepeaterType.ROOM_SERVER_STANDARD:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **repeater_type, **REPEATER_SETTINGS_LOCAL})
        elif self == RepeaterType.ROOM_SERVER_REPEAT_ENABLED:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **repeater_type, **REPEATER_SETTINGS_SUBURBAN})
        elif self == RepeaterType.ROOM_SERVER_MOBILE:
            return RepeaterSettings(**{**DEFAULT_REPEATER_SETTINGS, **repeater_type, **REPEATER_SETTINGS_MOBILE})
        else:
            raise ValueError(f"Unknown node type: {self.value}")
