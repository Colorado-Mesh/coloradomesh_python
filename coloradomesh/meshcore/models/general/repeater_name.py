from typing import Optional

from pydantic import model_validator

from coloradomesh.internal import BaseModel
from coloradomesh.meshcore.models.general.repeater_type import RepeaterType
from coloradomesh.meshcore.standards import REPEATER_NAMING_SCHEMA_ALT, REPEATER_NAMING_SCHEMA


class RepeaterName(BaseModel):
    """
    Contains elements of a MeshCore repeater on the ColoradoMesh network.
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
