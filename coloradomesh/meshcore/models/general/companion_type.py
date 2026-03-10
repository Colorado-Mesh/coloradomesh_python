import enum


class CompanionType(enum.Enum):
    """
    Enum representing the type of MeshCore companion node on the ColoradoMesh network.
    """
    PRIMARY = "Primary"
    SECONDARY = "Secondary"
    TERTIARY = "Tertiary"
    BACKUP = "Backup"
    EMERGENCY = "Emergency"
    MOBILE = "Mobile"
    VEHICLE = "Vehicle"
    HOME = "Home"

    @classmethod
    def to_acronym(cls, node_type: 'CompanionType') -> str:
        """
        Convert a CompanionType to its corresponding acronym.
        :param node_type: The CompanionType to convert.
        :type node_type: CompanionType
        :return: The corresponding acronym (<=4 characters)
        :rtype: str
        """
        if node_type == cls.PRIMARY:
            return "PRIM"
        elif node_type == cls.SECONDARY:
            return "SEC"
        elif node_type == cls.TERTIARY:
            return "TERT"
        elif node_type == cls.BACKUP:
            return "BACK"
        elif node_type == cls.EMERGENCY:
            return "EMER"
        elif node_type == cls.HOME:
            return "HOME"
        elif node_type == cls.MOBILE:
            return "MOB"
        elif node_type == cls.VEHICLE:
            return "VEH"
        else:
            raise ValueError(f"Unknown node type: {node_type}")
