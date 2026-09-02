import objectrest

from coloradomesh.meshcore.models.meshmapper.coverage import CoverageSummary

COLORADO_WAR_DRIVING_DATA = "https://raw.githubusercontent.com/Colorado-Mesh/coloradomesh_python/refs/heads/master/data/meshcore/nodes/coverage.json"


class WarDrivingService:
    def __init__(self):
        """
        Initialize the WarDrivingService by loading war driving data from the cached MeshMapper data.
        NOTE: Data will be automatically loaded and cached on initialization.
        """
        self.refresh_data()

    def _load_war_driving_data(self):
        """
        Load war driving data from the cached MeshMapper data and store it in the service instance.
        NOTE: This is an intensive operation, and should be called sparingly.
        """
        self._regions: list[CoverageSummary] = objectrest.get_object(url=COLORADO_WAR_DRIVING_DATA,  # type: ignore
                                                                     model=CoverageSummary,
                                                                     extract_list=True)

    def refresh_data(self):
        """
        Refresh the war driving data by reloading it from the cached MeshMapper data.
        NOTE: This data cache is repopulated at only set intervals, so refreshing may not actually pull new live data.
        """
        self._load_war_driving_data()

    def get_coverage_percentage(self) -> float:
        # Use the CO multi-region
        for region in self._regions:
            if region.region == 'CO':
                return region.coverage_percentage

        return 0.0
