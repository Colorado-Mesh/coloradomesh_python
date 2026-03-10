import re
from typing import Optional, Any

from pydantic import Field, field_validator

from coloradomesh.internal import BaseModel


class WarDrivingRepeater(BaseModel):
    id: str = Field(alias="id")
    signal_strength: float = Field(alias="signal_strength")
    latitude: float = Field(alias="latitude")
    longitude: float = Field(alias="longitude")

    @classmethod
    def from_heard_repeats_entry(cls, entry: str) -> 'WarDrivingRepeater':
        # Pattern: CODE(SIGNAL)[LAT, LON], e.g. AF(3.50)[39.8229, -105.0182]
        pattern = r'(\w{2})\(([-\d.]+)\)\[([-\d.]+),\s*([-\d.]+)\]'
        match = re.match(pattern, entry.strip())

        if not match:
            raise ValueError(f"Invalid repeater entry format: {entry}")

        _id, signal_strength, latitude, longitude = match.groups()

        return cls(
            id=_id,
            signal_strength=float(signal_strength),
            latitude=float(latitude),
            longitude=float(longitude)
        )

    @classmethod
    def from_via_entry(cls, entry: str) -> 'WarDrivingRepeater':
        # Pattern: CODE[LAT, LON], e.g. AF[39.8229, -105.0182]
        pattern = r'(\w{2})\s*\[([-\d.]+),\s*([-\d.]+)\]'
        match = re.match(pattern, entry.strip())

        if not match:
            raise ValueError(f"Invalid via entry format: {entry}")

        _id, latitude, longitude = match.groups()

        return cls(
            id=_id,
            signal_strength=0.0,  # No signal strength in via entries, set to 0.0 or None
            latitude=float(latitude),
            longitude=float(longitude)
        )


class WarDrivingEntry(BaseModel):
    latitude: float = Field(alias="lat")
    longitude: float = Field(alias="lon")
    observer: str = Field(alias="who")
    via__internal: Optional[str] = Field(alias="via", default=None)  # Is 'N/A' as None
    hr__internal: Optional[str] = Field(alias="repeats", default=None)  # Is 'None' as None
    power: str = Field(alias="power")  # e.g. '0.3w'
    status: int = Field(alias="status")  # TODO: What does this mean? Sometimes 5?
    date: int = Field(alias="date")  # Unix timestamp in seconds
    iata: str = Field(alias="iata")  # airport/map region code
    external_antenna: Optional[bool] = Field(alias="external_antenna",
                                             default=None)  # Comes in as "Yes" or "No", convert to bool
    noise_delta: Optional[int] = Field(alias="noise_delta", default=None)
    local_snr: Optional[float] = Field(alias="local_snr", default=None)
    local_rssi: Optional[float] = Field(alias="local_rssi", default=None)
    remote_snr: Optional[float] = Field(alias="remote_snr", default=None)
    noise_floor: Optional[int] = Field(alias="noisefloor",
                                       default=None)  # Comes in as string, e.g. "-113", convert to int
    public_key: Optional[str] = Field(alias="public_key", default=None)

    def __init__(self, /, **data: Any):
        super().__init__(**data)
        self._heard_repeaters = None
        self._via_repeaters = None

    @field_validator('via__internal', mode='before')
    @classmethod
    def validate_via(cls, value: Any) -> Optional[str]:
        if value is None:
            return None

        if isinstance(value, str):
            if value.lower() in ["n/a", "na", "none", "null", ""]:
                return None

            return value

        raise TypeError("Invalid via__internal value")

    @field_validator('hr__internal', mode='before')
    @classmethod
    def validate_heard_repeats(cls, value: Any) -> Optional[str]:
        if value is None:
            return None

        if isinstance(value, str):
            if value.lower() == "none":
                return None

            return value

        raise TypeError("Invalid hr__internal value")

    @field_validator('external_antenna', mode='before')
    @classmethod
    def validate_external_antenna(cls, value: Any) -> Optional[bool]:
        if value is None:
            return None

        if isinstance(value, bool):
            return value

        if isinstance(value, int):
            return bool(value)

        if isinstance(value, str):
            if value.lower() in ["yes", "true", "on"]:
                return True
            elif value.lower() in ["no", "false", "off"]:
                return False
            elif value.lower() in ["n/a", "na", "none", "null", ""]:
                return None

        raise ValueError(f"Invalid value for external_antenna: {value}")

    @field_validator('noise_floor', mode='before')
    @classmethod
    def validate_noise_floor(cls, value: Any) -> Optional[int]:
        if value is None:
            return None

        if isinstance(value, int):
            return value

        if isinstance(value, str):
            if not value:
                return None

            return int(value)

        raise ValueError(f"Invalid value for noise_floor: {value}")

    @property
    def via_repeaters(self) -> list[WarDrivingRepeater]:
        def _parse_via_repeaters() -> list[WarDrivingRepeater]:
            _via = self.via__internal
            if not _via:
                return []

            # Entry could be in the format "Direct, CODE[LAT, LON]"
            # Ignore the "Direct" entry and parse the rest as repeaters
            elements = _via.split(", ")
            return [
                WarDrivingRepeater.from_via_entry(entry)
                for entry in elements
                if entry.strip() and entry.strip().lower() != "direct"
            ]

        if self._via_repeaters is None:
            self._via_repeaters = _parse_via_repeaters()

        return self._via_repeaters

    @property
    def heard_repeaters(self) -> list[WarDrivingRepeater]:
        def _parse_heard_repeaters() -> list[WarDrivingRepeater]:
            _heard_repeats = self.hr__internal
            if not _heard_repeats:
                return []

            return [
                WarDrivingRepeater.from_heard_repeats_entry(entry)
                for entry in _heard_repeats.split(", ") if entry.strip()
            ]

        if self._heard_repeaters is None:
            self._heard_repeaters = _parse_heard_repeaters()

        return self._heard_repeaters

    def location_matches(self, latitude: float, longitude: float) -> bool:
        """
        Check if the given latitude and longitude match the location of this WarDrivingEntry
        :param latitude: The latitude to compare.
        :param longitude: The longitude to compare.
        :return: True if the given location matches the location of this WarDrivingEntry, False otherwise.
        :rtype: bool
        """
        return self.latitude == latitude and self.longitude == longitude
