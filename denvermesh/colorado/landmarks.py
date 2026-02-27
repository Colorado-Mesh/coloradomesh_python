from typing import Any

from denvermesh.colorado._base import _PlaceEnum, _Place, PlaceAbbreviations


class Landmark(_Place):
    regions: list[_PlaceEnum]

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class Landmarks(_PlaceEnum):
    PIKES_PEAK = Landmark(
        name="Pikes Peak",
        abbreviations=PlaceAbbreviations(
            three_letter="PPK",
            five_letter="PIKES",
            seven_letter="PIKESPK",
            fourteen_letter="PIKES PEAK"
        ),
        regions=[]
    )

    @property
    def regions(self) -> list[_PlaceEnum]:
        """
        Get the list a regions that this landmark is located in.
        :return: A list of regions that this landmark is located in.
        """
        return self._place.regions  # type: ignore
