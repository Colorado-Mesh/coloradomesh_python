import enum
from typing import Any

from colorado import Municipalities, Airports
from coloradomesh.internal import BaseModel


class Region(BaseModel):
    """
    Represents a MeshCore region on the ColoradoMesh network.
    """

    airport: Airports
    """
    The airport that serves this region.
    """

    _cached_municipalities: list[Municipalities] = []

    @property
    def name(self) -> str:
        """
        Get the name of the region, which is the name of the nearest airport to this region.
        :return: Name of the region.
        """
        return self.airport.name

    @property
    def code(self) -> str:
        """
        Get the code for this region, which is the same as the IATA code for the airport that serves this region.
        :return: The code for this region.
        :rtype: str
        """
        return self.airport.iata_code.lower()

    @property
    def municipalities(self) -> Municipalities:
        """
        Get the municipalities that are served by this region.
        :return: The municipalities that are served by this region.
        :rtype: Municipalities
        """
        if not self._cached_municipalities:
            self._cached_municipalities = [mun for mun in Municipalities if mun.nearest_airport == self.airport]

        return self._cached_municipalities

    def __init__(self, /, **data: Any):
        super().__init__(**data)


class Regions(enum.Enum):
    ASE = Region(
        airport=Airports.ASPEN_PITKIN,
    )
    COS = Region(
        airport=Airports.COLORADO_SPRINGS,
    )
    CEZ = Region(
        airport=Airports.CORTEZ,
    )
    DEN = Region(
        airport=Airports.DENVER,
    )
    DRO = Region(
        airport=Airports.DURANGO_LA_PLATA,
    )
    EGE = Region(
        airport=Airports.EAGLE,
    )
    GJT = Region(
        airport=Airports.GRAND_JUNCTION,
    )
    GUC = Region(
        airport=Airports.GUNNISON_CRESTED_BUTTE,
    )
    MTJ = Region(
        airport=Airports.MONTROSE,
    )
    FNL = Region(
        airport=Airports.NORTHERN_COLORADO,
    )
    PUB = Region(
        airport=Airports.PUEBLO,
    )
    ALS = Region(
        airport=Airports.SAN_LUIS_VALLEY,
    )
    LAA = Region(
        airport=Airports.SOUTHEAST_COLORADO,
    )
    STK = Region(
        airport=Airports.STERLING,
    )
    TEX = Region(
        airport=Airports.TELLURIDE,
    )
    HDN = Region(
        airport=Airports.YAMPA_VALLEY,
    )

    def __init__(self, region: Region):
        self._region = region

    @property
    def name(self) -> str:
        """
        Get the name of the region, which is the name of the nearest airport to this region.
        :return: Name of the region.
        """
        return self._region.name

    @property
    def code(self) -> str:
        """
        Get the code for this region, which is the same as the IATA code for the airport that serves this region.
        :return: The code for this region.
        :rtype: str
        """
        return self._region.code

    @property
    def municipalities(self) -> Municipalities:
        """
        Get the municipalities that are served by this region.
        :return: The municipalities that are served by this region.
        :rtype: Municipalities
        """
        return self._region.municipalities

    @classmethod
    def all_codes(cls) -> list[str]:
        """
        Get a list of all region codes.
        :return: A list of all region codes.
        :rtype: list[str]
        """
        return [region.code for region in cls]

    @classmethod
    def from_code(cls, code: str) -> 'Regions':
        """
        Get a Regions enum member from a region code.
        :param code: The region code to look up.
        :return: The Regions enum member corresponding to the given code.
        :rtype: Regions
        :raises ValueError: If no region with the given code is found.
        """
        for region in cls:
            if region.code == code.lower():
                return region
        raise ValueError(f"No region found with code '{code}'")
