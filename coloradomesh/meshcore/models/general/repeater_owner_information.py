from typing import Optional

from coloradomesh.internal import BaseModel


class RepeaterOwnerInformation(BaseModel):
    """
    Contains elements of the owner information for a MeshCore repeater on the ColoradoMesh network.
    """
    handle: str  # Callsign or handle — your ham callsign or Discord username
    antenna_type: Optional[str]  # Antenna specs — type, gain, height above ground
    power_source: Optional[str]  # Power source — mains, solar, battery backup
    install_type: Optional[str]  # Install type — rooftop, tower, indoor, portable

    @property
    def formatted(self) -> str:
        """
        Get the formatted owner information string based on the provided details.
        :return: A formatted string containing the owner information for a MeshCore repeater on the ColoradoMesh network.
        :rtype: str
        """
        details = [self.handle]
        if self.antenna_type:
            details.append(self.antenna_type)
        if self.power_source:
            details.append(self.power_source)
        if self.install_type:
            details.append(self.install_type)
        return " | ".join(details)

    @property
    def set_owner_info_command(self) -> str:
        return f"set owner.info '{self.formatted}'"
