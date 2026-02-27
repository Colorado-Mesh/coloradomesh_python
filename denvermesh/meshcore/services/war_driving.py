import objectrest

from denvermesh.meshcore.models.meshmapper.war_driving_entry import WarDrivingEntry, WarDrivingRepeater

DENVER_WAR_DRIVING_DATA = "https://den.meshmapper.net/api.php?request=map_data"


class WarDrivingService:
    def __init__(self):
        """
        Initialize the WarDrivingService by loading war driving data from the MeshMapper API.
        NOTE: Data will be automatically loaded and cached on initialization.
        """
        self.refresh_data()

    def _load_war_driving_data(self):
        """
        Load war driving data from the MeshMapper API and store it in the service instance.
        NOTE: This is an intensive operation, and should be called sparingly.
        """
        self._entries: list[WarDrivingEntry] = objectrest.get_object(url=DENVER_WAR_DRIVING_DATA,  # type: ignore
                                                                     model=WarDrivingEntry,
                                                                     extract_list=True)
        # Build spatial hash map for O(1) lookups
        self._location_index: dict[tuple[float, float], list[WarDrivingEntry]] = {}
        for entry in self._entries:
            key = (entry.latitude, entry.longitude)
            if key not in self._location_index:
                self._location_index[key] = []
            self._location_index[key].append(entry)

    def refresh_data(self):
        """
        Refresh the war driving data by reloading it from the MeshMapper API.
        """
        self._load_war_driving_data()

    def coverage_at_location(self, latitude: float, longitude: float) -> list[WarDrivingRepeater]:
        """
        Get a list of repeaters heard or via repeaters at the provided latitude and longitude based on the war driving data.
        :param latitude: The latitude to check for coverage.
        :param longitude: The longitude to check for coverage.
        :return: A list of WarDrivingRepeater objects representing the repeaters heard or via repeaters at the location. If there is no coverage, an empty list is returned.
        """
        location_entries: list[WarDrivingEntry] = self._location_index.get((latitude, longitude), [])
        repeaters: list[WarDrivingRepeater] = []
        for entry in location_entries:
            repeaters.extend(entry.heard_repeaters)
            repeaters.extend(entry.via_repeaters)
        return repeaters

    def check_coverage(self, latitude: float, longitude: float) -> bool:
        """
        Check if the provided latitude and longitude has coverage based on the war driving data.
        :param latitude: The latitude to check for coverage.
        :param longitude: The longitude to check for coverage.
        :return: True if the location has coverage (i.e., there is at least one war driving entry with heard or via repeaters at the location), False otherwise.
        :rtype: bool
        """
        return len(self.coverage_at_location(latitude=latitude, longitude=longitude)) > 0
