from typing import Any

from denvermesh.colorado._base import _PlaceEnum, _Place, PlaceAbbreviations
from denvermesh.colorado.municipalities import Municipalities


class Airport(_Place):
    iata_code: str
    regions: list[_PlaceEnum]

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class Airports(_PlaceEnum):
    ASPEN = Airport(
        name="Aspen-Pitkin County Airport",
        iata_code="ASE",
        abbreviations=PlaceAbbreviations(
            three_letter="ASE",
            five_letter="ASE",
            seven_letter="ASE",
            fourteen_letter="ASE"
        ),
        regions=[Municipalities.ASPEN])
    COLORADO_SPRINGS = Airport(
        name="City of Colorado Springs Municipal Airport",
        iata_code="COS",
        abbreviations=PlaceAbbreviations(
            three_letter="COS",
            five_letter="COS",
            seven_letter="COS",
            fourteen_letter="COS"
        ),
        regions=[Municipalities.COLORADO_SPRINGS])
    CORTEZ = Airport(
        name="Cortez Municipal Airport",
        iata_code="CEZ",
        abbreviations=PlaceAbbreviations(
            three_letter="CEZ",
            five_letter="CEZ",
            seven_letter="CEZ",
            fourteen_letter="CEZ"
        ),
        regions=[Municipalities.CORTEZ])
    DENVER = Airport(
        name="Denver International Airport",
        iata_code="DEN",
        abbreviations=PlaceAbbreviations(
            three_letter="DEN",
            five_letter="DEN",
            seven_letter="DEN",
            fourteen_letter="DEN"
        ),
        regions=[Municipalities.DENVER])
    DURANGO_LA_PLATA = Airport(
        name="Durango-La Plata County Airport",
        iata_code="DRO",
        abbreviations=PlaceAbbreviations(
            three_letter="DRO",
            five_letter="DRO",
            seven_letter="DRO",
            fourteen_letter="DRO"
        ),
        regions=[Municipalities.DURANGO])
    EAGLE = Airport(
        name="Eagle County Regional Airport",
        iata_code="EGE",
        abbreviations=PlaceAbbreviations(
            three_letter="EGE",
            five_letter="EGE",
            seven_letter="EGE",
            fourteen_letter="EGE"
        ),
        regions=[Municipalities.EAGLE, Municipalities.VAIL])
    GRAND_JUNCTION = Airport(
        name="Grand Junction Regional Airport",
        iata_code="GJT",
        abbreviations=PlaceAbbreviations(
            three_letter="GJT",
            five_letter="GJT",
            seven_letter="GJT",
            fourteen_letter="GJT"
        ),
        regions=[Municipalities.GRAND_JUNCTION])
    GUNNISON_CRESTED_BUTTE = Airport(
        name="Gunnison-Crested Butte Regional Airport",
        iata_code="GUC",
        abbreviations=PlaceAbbreviations(
            three_letter="GUC",
            five_letter="GUC",
            seven_letter="GUC",
            fourteen_letter="GUC"
        ),
        regions=[Municipalities.GUNNISON, Municipalities.CRESTED_BUTTE])
    MONTROSE = Airport(
        name="Montrose Regional Airport",
        iata_code="MTJ",
        abbreviations=PlaceAbbreviations(
            three_letter="MTJ",
            five_letter="MTJ",
            seven_letter="MTJ",
            fourteen_letter="MTJ"
        ),
        regions=[Municipalities.MONTROSE])
    NORTHERN_COLORADO = Airport(
        name="Northern Colorado Regional Airport",
        iata_code="FNL",
        abbreviations=PlaceAbbreviations(
            three_letter="FNL",
            five_letter="FNL",
            seven_letter="FNL",
            fourteen_letter="FNL"
        ),
        regions=[Municipalities.FORT_COLLINS, Municipalities.LOVELAND])
    PUEBLO = Airport(
        name="Pueblo Memorial Airport",
        iata_code="PUB",
        abbreviations=PlaceAbbreviations(
            three_letter="PUB",
            five_letter="PUB",
            seven_letter="PUB",
            fourteen_letter="PUB"
        ),
        regions=[Municipalities.PUEBLO])
    SAN_LUIS_VALLEY = Airport(
        name="San Luis Valley Regional Airport",
        iata_code="ALS",
        abbreviations=PlaceAbbreviations(
            three_letter="ALS",
            five_letter="ALS",
            seven_letter="ALS",
            fourteen_letter="ALS"
        ),
        regions=[Municipalities.ALAMOSA])
    TELLURIDE = Airport(
        name="Telluride Regional Airport",
        iata_code="TEX",
        abbreviations=PlaceAbbreviations(
            three_letter="TEX",
            five_letter="TEX",
            seven_letter="TEX",
            fourteen_letter="TEX"
        ),
        regions=[Municipalities.TELLURIDE])
    YAMPA_VALLEY = Airport(
        name="Yampa Valley Regional Airport",
        iata_code="HDN",
        abbreviations=PlaceAbbreviations(
            three_letter="HDN",
            five_letter="HDN",
            seven_letter="HDN",
            fourteen_letter="HDN"
        ),
        regions=[Municipalities.HAYDEN])

    @property
    def iata_code(self) -> str:
        return self._place.iata_code  # type: ignore

    @property
    def regions(self) -> list[_PlaceEnum]:
        """
        Get the list a regions that this airport is located in.
        :return: A list of regions that this airport is located in.
        """
        return self._place.regions  # type: ignore
