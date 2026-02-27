from typing import Any

from denvermesh.colorado._base import _Place, _PlaceEnum, PlaceAbbreviations


class UnincorporatedArea(_Place):
    def __init__(self, /, **data: Any):
        super().__init__(**data)


class UnincorporatedAreas(_PlaceEnum):
    HIGHLANDS_RANCH = UnincorporatedArea(
        name="Highlands Ranch",
        abbreviations=PlaceAbbreviations(
            three_letter="HLD",
            five_letter="HGHLN",
            seven_letter="HGHLND",
            fourteen_letter="HIGHLANDSRANCH"
        )
    )
    HENDERSON = UnincorporatedArea(
        name="Henderson",
        abbreviations=PlaceAbbreviations(
            three_letter="HND",
            five_letter="HENDR",
            seven_letter="HENDRSN",
            fourteen_letter="HENDERSON"
        )
    )
