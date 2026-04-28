from typing import Optional

from pydantic import model_validator

from coloradomesh.internal import BaseModel
from coloradomesh.meshcore.models.general.repeater_type import RepeaterType
from coloradomesh.meshcore.standards import REPEATER_NAMING_SCHEMA_ALT, REPEATER_NAMING_SCHEMA


class RepeaterName(BaseModel):
    """
    Contains elements of a MeshCore repeater on the Colorado Mesh network.
    """
    repeater_type: RepeaterType
    region: str
    landmark: str  # <=5-char landmark code if city is provided, <=11-char landmark code if city is not provided
    public_key_id: str = None
    city: Optional[str] = None  # <=5-char city code, optional since some locations may not be within a city

    @model_validator(mode="after")
    def validate_model(self):
        # Need either <=5 city and <=5 landmark, or a <=11 landmark
        if self.city:
            if len(self.city) > 5:
                raise ValueError("City code must be up to 5 characters long")
            if len(self.landmark) > 5:
                raise ValueError("Landmark code must be up to 5 characters long")
        elif len(self.landmark) > 11:
            raise ValueError("Landmark code must be up to 11 characters long if city code is not provided")

        return self

    @property
    def formatted(self) -> str:
        """
        Get the formatted companion name based on the provided details.
        :return: A formatted companion name based on the provided details.
        :rtype: str
        """
        suffix = RepeaterType.to_acronym(node_type=self.repeater_type)

        if not self.city:
            return REPEATER_NAMING_SCHEMA_ALT.format(
                region=self.region.upper(),
                landmark=self.landmark,  # Not automatically uppercased
                type=suffix.upper(),
                pub_key_id=self.public_key_id.upper()
            )
        else:
            return REPEATER_NAMING_SCHEMA.format(
                region=self.region.upper(),
                city=self.city.upper(),
                landmark=self.landmark,  # Not automatically uppercased
                type=suffix.upper(),
                pub_key_id=self.public_key_id.upper()
            )

    @classmethod
    def from_name_string(cls, name_string: str) -> 'RepeaterName':
        """
        Attempts to create a RepeaterName object from a name string.
        :param name_string: The name to parse.
        :return: A RepeaterName object.
        :raises ValueError: If the name string is invalid or does not follow the naming schema.
        """
        try:
            segments: list[str] = name_string.strip().split("-")
            assert len(segments) in [4, 5]  # Should be four or five segments, will raise if not

            region_string = segments[0]
            # Second (+ third) segment should be city + landmark, or just landmark
            if len(segments) == 5:
                city = segments[1]
                landmark = segments[2]
            else:
                city = None
                landmark = segments[1]
            public_key_id = segments[-1]
            repeater_type_string = segments[-2]
            repeater_type: RepeaterType = RepeaterType.from_text(repeater_type_string)  # Will raise if cannot parse

            return RepeaterName(  # Will raise if cannot validate
                **dict(
                    repeater_type=repeater_type,
                    region=region_string,
                    landmark=landmark,
                    public_key_id=public_key_id,
                    city=city
                )
            )
        except:
            raise ValueError("Invalid name string")
