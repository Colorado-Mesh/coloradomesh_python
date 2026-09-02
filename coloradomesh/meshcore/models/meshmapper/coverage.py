from typing import Optional, List

from pydantic import Field

from coloradomesh.internal import BaseModel


class CoverageSummaryGridSize(BaseModel):
    lat: float = Field(alias="lat")
    lon: float = Field(alias="lon")


class CoverageSummaryTypeCounts(BaseModel):
    bidirectional: Optional[int] = Field(alias="BIDIR")
    tx: Optional[int] = Field(alias="TX")
    rx: Optional[int] = Field(alias="RX")
    discovery: Optional[int] = Field(alias="DISC")
    dead: Optional[int] = Field(alias="DEAD")
    drop: Optional[int] = Field(alias="DROP")


class CoverageSummaryTypeBits(BaseModel):
    bidirectional: Optional[int] = Field(alias="BIDIR")
    tx: Optional[int] = Field(alias="TX")
    rx: Optional[int] = Field(alias="RX")
    discovery: Optional[int] = Field(alias="DISC")
    dead: Optional[int] = Field(alias="DEAD")
    drop: Optional[int] = Field(alias="DROP")


class CoverageSummaryMapBounds(BaseModel):
    minimum_latitude: float = Field(alias="minLat")
    minimum_longitude: float = Field(alias="minLon")
    maximum_latitude: float = Field(alias="maxLat")
    maximum_longitude: float = Field(alias="maxLon")


class CoverageGridSquareBounds(BaseModel):
    south: float = Field(alias="south")
    north: float = Field(alias="north")
    east: float = Field(alias="east")
    west: float = Field(alias="west")


class CoverageGridSquare(BaseModel):
    id: str = Field(alias="grid_id")
    bounds: CoverageGridSquareBounds = Field(alias="bounds")
    coverage_type: Optional[str] = Field(alias="coverage_type")
    fill_color: str = Field(alias="fill_color")
    border_color: str = Field(alias="border_color")
    snr: Optional[float] = Field(alias="snr")
    timestamp: Optional[float] = Field(alias="timestamp")  # UNIX timestamp
    count: int = Field(alias="count")
    snr_min: Optional[float] = Field(alias="snr_min")
    snr_max: Optional[float] = Field(alias="snr_max")
    status_mask: int = Field(alias="status_mask")
    first_seen: Optional[float] = Field(alias="first_seen")  # UNIX timestamp
    noise: Optional[float] = Field(alias="noise")
    effective: float = Field(alias="effective")


class CoverageSummary(BaseModel):
    success: bool = Field(alias="success")
    region: str = Field(alias="region")
    region_name: str = Field(alias="region_name")
    grid_size: CoverageSummaryGridSize = Field(alias="grid_size")
    schema_version: int = Field(alias="schema_version")
    generated_at: float = Field(alias="generated_at")  # UNIX timestamp
    data_age_seconds: int = Field(alias="data_age_seconds")
    total_squares: int = Field(alias="total_squares")
    point_count: int = Field(alias="point_count")
    coverage_type_counts: CoverageSummaryTypeCounts = Field(alias="coverage_type_counts")
    coverage_type_bits: CoverageSummaryTypeBits = Field(alias="type_bits")
    coverage_map_bounds: CoverageSummaryMapBounds = Field(alias="bbox")
    grid_squares: List[CoverageGridSquare] = Field(alias="grid_squares")

    @property
    def coverage_percentage(self) -> float:
        # Sum of BIDIR + TX + RX + DISC / total grid squares
        return sum(
            [
                self.coverage_type_counts.bidirectional or 0,
                self.coverage_type_counts.tx or 0,
                self.coverage_type_counts.rx or 0,
                self.coverage_type_counts.discovery or 0,
            ]
        ) / self.total_squares
