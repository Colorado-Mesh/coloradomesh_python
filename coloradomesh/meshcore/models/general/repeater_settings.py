from typing import Optional

from pydantic import model_validator, Field

from coloradomesh.internal import BaseModel
from coloradomesh.meshcore.models.general.repeater_owner_information import RepeaterOwnerInformation


def _prefix_byte_size_to_path_hash_mode(prefix_size: int) -> int:
    if prefix_size == 1:
        return 0
    if prefix_size == 2:
        return 1
    if prefix_size == 3:
        return 2

    raise ValueError("prefix_size must be one of 1, 2, or 3")


class RepeaterRegionSettings(BaseModel):
    all: list[str] = Field(alias="all")
    home: Optional[str] = Field(alias="home")

    @model_validator(mode="after")
    def validate_model(self):
        # Home region must be one of the regions in the all list, if specified
        if self.home and self.home not in self.all:
            raise ValueError("Home region must be one of the regions in the all list")
        return self

    @property
    def add_region_commands(self) -> list[str]:
        return [f"region put {region}" for region in self.all]

    @property
    def add_home_region_command(self) -> Optional[str]:
        if self.home:
            return f"region home {self.home}"

        return None

    @property
    def save_regions_command(self) -> str:
        return "region save"


class RepeaterSettings(BaseModel):
    txdelay: Optional[float] = Field(
        alias="txdelay", default=None)  # Wait before retransmitting floods. Higher = defer to other nodes
    direct_txdelay: Optional[float] = Field(
        alias="direct.txdelay", default=None)  # Wait before retransmitting direct packets. Usually lower than txdelay
    rxdelay: Optional[float] = Field(alias="rxdelay",
                                     default=None)  # SNR-based processing priority. Higher = prefer stronger signal
    advert_interval: Optional[int] = Field(alias="advert.interval", default=None)  # Local advert in minutes
    flood_advert_interval: Optional[int] = Field(alias="flood.advert.interval", default=None)  # Flood advert in hours
    admin_password: Optional[str] = Field(alias="password", default=None)  # Admin password
    guest_password: Optional[str] = Field(alias="guest.password", default=None)  # Guest password for telemetry access
    name: Optional[str] = Field(alias="name",
                                default=None)  # Name of the repeater, used for identification in the network
    owner_info: Optional[RepeaterOwnerInformation] = Field(alias="owner",
                                                           default=None)  # Owner information string for this repeater
    private_key: Optional[str] = Field(
        alias="prv.key", default=None)  # Private key for this repeater
    regions: Optional[RepeaterRegionSettings] = Field(alias="regions",
                                                      default=None)  # Region settings for this repeater
    repeater_type: Optional[int] = Field(alias="repeater_type", default=None)  # Repeater type
    prefix_size: Optional[int] = Field(alias="prefix_size", default=None)  # Prefix byte size

    @model_validator(mode="after")
    def validate_model(self):
        if not 0.0 <= self.txdelay <= 3.0:
            raise ValueError("txdelay must be between 0.0 and 3.0 seconds")
        if not 0.0 <= self.direct_txdelay <= 3.0:
            raise ValueError("direct_txdelay must be between 0.0 and 3.0 seconds")
        if not 0.0 <= self.rxdelay <= 20.0:
            raise ValueError("rxdelay must be between 0.0 and 20.0 seconds")
        if not self.prefix_size in [1, 2, 3]:
            raise ValueError("prefix_size must be one of 1, 2, or 3")

        return self

    def to_json(self) -> dict:
        return self.model_dump(by_alias=True)

    @property
    def set_txdelay_command(self) -> Optional[str]:
        if self.txdelay:
            return f"set txdelay {self.txdelay:.2f}"
        return None

    @property
    def set_direct_txdelay_command(self) -> Optional[str]:
        if self.direct_txdelay:
            return f"set direct.txdelay {self.direct_txdelay:.2f}"
        return None

    @property
    def set_rxdelay_command(self) -> Optional[str]:
        if self.rxdelay:
            return f"set rxdelay {self.rxdelay:.2f}"
        return None

    @property
    def set_advert_interval_command(self) -> Optional[str]:
        if self.advert_interval:
            return f"set advert.interval {self.advert_interval}"
        return None

    @property
    def set_flood_advert_interval_command(self) -> Optional[str]:
        if self.flood_advert_interval:
            return f"set flood.advert.interval {self.flood_advert_interval}"
        return None

    @property
    def set_admin_password_command(self) -> Optional[str]:
        # Blank admin password is a bad idea, not allowed
        if not self.admin_password:
            return None

        return f"password {self.admin_password}"

    @property
    def set_guest_password_command(self) -> Optional[str]:
        if self.guest_password:
            return f"set guest.password {self.guest_password}"

        # Allow empty/blank gues password
        if self.guest_password == "":
            return f"set guest.password "  # Empty space to set blank password

        return None

    @property
    def set_name_command(self) -> Optional[str]:
        if self.name:
            return f"set name {self.name}"  # This should be fine since the naming standard has no spaces
        return None

    @property
    def set_owner_info_command(self) -> Optional[str]:
        if self.owner_info is not None:  # Allow empty string as a valid value
            return self.owner_info.set_owner_info_command
        return None

    @property
    def set_private_key_command(self) -> Optional[str]:
        if self.private_key:
            return f"set prv.key {self.private_key}"
        return None

    @property
    def add_region_commands(self) -> Optional[list[str]]:
        if not self.regions:
            return None

        return self.regions.add_region_commands

    @property
    def add_home_region_command(self) -> Optional[str]:
        if not self.regions:
            return None

        return self.regions.add_home_region_command

    @property
    def save_regions_command(self) -> Optional[str]:
        if not self.regions:
            return None

        return self.regions.save_regions_command

    @property
    def save_regions_commands(self) -> Optional[str]:
        """
        Backwards compatibility for save_regions_command.
        Please use save_regions_command instead of save_regions_commands in new code, as the singular form is more consistent with the other command properties.
        :return:
        """
        return self.save_regions_command

    @property
    def set_path_hash_size_command(self) -> Optional[str]:
        if self.prefix_size:
            return f"set path.hash.size {_prefix_byte_size_to_path_hash_mode(self.prefix_size)}"
        return None
