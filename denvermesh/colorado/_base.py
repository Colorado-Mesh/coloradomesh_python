import enum
from typing import Any

from pydantic import model_validator

from denvermesh.internal import BaseModel


class PlaceAbbreviations(BaseModel):
    three_letter: str
    five_letter: str
    seven_letter: str
    fourteen_letter: str

    def __init__(self, /, **data: Any):
        super().__init__(**data)

    @model_validator(mode="after")
    def validate_model(self):
        lengths = {
            'three_letter': 3,
            'five_letter': 5,
            'seven_letter': 7,
            'fourteen_letter': 14
        }
        # Validate that the abbreviations are all uppercase and have the correct lengths
        for attr_name, expected_length in lengths.items():
            attr_value = getattr(self, attr_name)

            if not isinstance(attr_value, str):
                raise ValueError(f"{attr_name} must be a string")

            if not attr_value.isupper():
                raise ValueError(f"{attr_name} must be uppercase")

            if not len(attr_value) <= expected_length:
                raise ValueError(f"{attr_name} must be <={expected_length} characters long")

        return self


class _Place(BaseModel):
    name: str
    abbreviations: PlaceAbbreviations

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class _PlaceEnum(enum.Enum):
    def __init__(self, place: _Place):
        self._place = place

    @property
    def name(self) -> str:
        return self._place.name

    @property
    def abbreviations(self) -> PlaceAbbreviations:
        return self._place.abbreviations
