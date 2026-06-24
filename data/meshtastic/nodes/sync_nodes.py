import argparse
import json
import os
from datetime import datetime
from typing import Optional

import objectrest
from pydantic import BaseModel, Field

from coloradomesh.colorado import COLORADO
from coloradomesh.meshtastic.models.general import Node, NodeRole

MESHMAP_URL = "https://meshmap.net/nodes.json"  # All Meshtastic devices globally
LIAMCOTTLE_MESHTASTIC_URL = "https://meshtastic.liamcottle.net/api/v1/nodes"  # All Meshtastic devices globally
CM_MESHVIEW_URL = "https://map.meshtastic.coloradomesh.org/api/nodes?days_active=3"  # All ACTIVE Meshtastic devices heard on the msh/US/CO topic

_COLORADO = COLORADO

COLORADO_MSH_TOPIC = "msh/US/CO"


### MeshMap-specific models for parsing API responses
class MeshMapNode(BaseModel):
    id: Optional[int] = Field(alias="id", default=None)
    long_name: str = Field(alias="longName")
    short_name: str = Field(alias="shortName")
    hardware_model: Optional[str] = Field(alias="hwModel", default=None)
    role: Optional[str] = Field(alias="role", default=None)
    latitude: Optional[float] = Field(alias="latitude", default=None)
    longitude: Optional[float] = Field(alias="longitude", default=None)
    altitude: Optional[float] = Field(alias="altitude", default=None)
    precision: Optional[int] = Field(alias="precision", default=None)
    seen_by: Optional[dict] = Field(alias="seenBy", default=None)

    # This is unused because it would be too intensive to iterate through all global nodes to check there seenBy lists
    @property
    def seen_by_colorado_mqtt_topic(self) -> bool:
        if not self.seen_by:
            return False

        for key, value in self.seen_by.items():
            if key.startswith(COLORADO_MSH_TOPIC):
                return True

        return False

    @property
    def real_latitude(self) -> Optional[float]:
        # Move decimal seven digits to the left
        return (float(self.latitude) / 10_000_000) if self.latitude else None

    @property
    def real_longitude(self) -> Optional[float]:
        return (float(self.longitude) / 10_000_000) if self.longitude else None

    @property
    def node_role(self) -> NodeRole:
        return NodeRole.from_name(name=self.role) if self.role is not None else NodeRole.UNKNOWN

    def to_node(self) -> Node:
        return Node(
            id=self.id,
            long_name=self.long_name,
            short_name=self.short_name,
            hardware_model=self.hardware_model,
            role=self.node_role,
            latitude=self.real_latitude,
            longitude=self.real_longitude,
            altitude=self.altitude,
            precision=self.precision
        )


def _meshmap_node_in_colorado(node: MeshMapNode) -> bool:
    """
    Return true if MeshMapNode is in Colorado.
    :param node: The MeshMapNode to check.
    :return: True if the node is in Colorado, False otherwise.
    """
    if not node:
        return False

    if not all([node.real_latitude, node.real_longitude]):
        return False

    return _COLORADO.coordinates_within_borders(latitude=node.real_latitude, longitude=node.real_longitude)


def _get_meshmap_nodes() -> list[MeshMapNode]:
    """
    Fetch all nodes from the MeshMap API.
    Filters nodes to just those with lat/lon inside Colorado borders.
    :rtype: list[MeshMapNode]
    """
    all_nodes_data: dict = objectrest.get_object(url=MESHMAP_URL,  # type: ignore
                                                 model=dict)
    if not all_nodes_data:
        # We don't want to return an empty list, that would effectively erase the previous data snapshot
        # Instead, consider this run failed
        raise Exception(f"Could not load nodes from MeshMap")

    all_nodes: list[MeshMapNode] = [
        MeshMapNode(id=node_id, **node_data) for (node_id, node_data) in all_nodes_data.items()
    ]
    if not all_nodes:
        # We don't want to return an empty list, that would effectively erase the previous data snapshot
        # Instead, consider this run failed
        raise Exception(f"Could not load nodes from MeshMap")

    print(
        f"Found {len(all_nodes)} nodes from MeshMap, filtering to find those with lat/lon inside Colorado")

    # Rough filter to only nodes in Colorado + padding, to cut down on number of nodes
    # that will do exact polygon math
    # This rapidly brings it down from global nodes to those that might ACTUALLY be in Colorado
    lat_min = 36
    lat_max = 41.5
    lon_min = -110
    lon_max = -101
    print(
        f"Applying pre-filter to nodes with lat between {lat_min} and {lat_max} and lon between {lon_min} and {lon_max}")
    prefiltered_nodes: list[MeshMapNode] = [
        node for node in all_nodes if (
                all([node.real_latitude, node.real_longitude]) and
                all([(lat_min <= node.real_latitude <= lat_max), (lon_min <= node.real_longitude <= lon_max)])
        )
    ]

    print(
        f"Checking remaining {len(prefiltered_nodes)} nodes for exact Colorado presence"
    )
    filtered_nodes: list[MeshMapNode] = [
        node for node in prefiltered_nodes if _meshmap_node_in_colorado(node=node)
    ]

    print(f"Found {len(filtered_nodes)} nodes in Colorado via MeshMap")
    return filtered_nodes


### Liam Cottle Meshtastic Map-specific models for parsing API responses
class LiamCottleMeshtasticNode(BaseModel):
    id: Optional[int] = Field(alias="id", default=None)
    node_id: Optional[int] = Field(alias="node_id", default=None)
    long_name: str = Field(alias="long_name")
    short_name: str = Field(alias="short_name")
    hardware_model: Optional[int] = Field(alias="hardware_model", default=None)
    hardware_model_name: Optional[str] = Field(alias="hardware_model_name", default=None)
    role: Optional[int] = Field(alias="role", default=None)
    role_name: Optional[str] = Field(alias="role_name", default=None)
    latitude: Optional[float] = Field(alias="latitude", default=None)
    longitude: Optional[float] = Field(alias="longitude", default=None)
    altitude: Optional[float] = Field(alias="altitude", default=None)
    position_precision: Optional[int] = Field(alias="position_precision", default=None)
    position_updated_at: Optional[str] = Field(alias="position_updated_at", default=None)
    created_at: Optional[datetime] = Field(alias="created_at", default=None)
    updated_at: Optional[datetime] = Field(alias="updated_at", default=None)
    region_name: Optional[str] = Field(alias="region_name", default=None)
    mqtt_connection_state_updated_at: Optional[datetime] = Field(alias="mqtt_connection_state_updated_at", default=None)

    # Plus a bunch more irrelevant data

    @property
    def real_latitude(self) -> Optional[float]:
        # Move decimal seven digits to the left
        return (float(self.latitude) / 10_000_000) if self.latitude else None

    @property
    def real_longitude(self) -> Optional[float]:
        return (float(self.longitude) / 10_000_000) if self.longitude else None

    @property
    def node_role(self) -> NodeRole:
        return NodeRole.from_int(self.role) if self.role is not None else NodeRole.UNKNOWN

    def to_node(self) -> Node:
        return Node(
            id=self.id,
            long_name=self.long_name,
            short_name=self.short_name,
            hardware_model=self.hardware_model_name,
            role=self.node_role,
            latitude=self.real_latitude,
            longitude=self.real_longitude,
            altitude=self.altitude,
            precision=self.position_precision,
        )


def _liam_cottle_node_in_colorado(node: LiamCottleMeshtasticNode) -> bool:
    """
    Return true if LiamCottleMeshtasticNode is in Colorado.
    :param node: The LiamCottleMeshtasticNode to check.
    :return: True if the node is in Colorado, False otherwise.
    """
    if not node:
        return False

    if not all([node.real_latitude, node.real_longitude]):
        return False

    return _COLORADO.coordinates_within_borders(latitude=node.real_latitude, longitude=node.real_longitude)


def _get_liam_cottle_nodes() -> list[LiamCottleMeshtasticNode]:
    """
    Fetch all nodes from the Liam Cottle Meshtastic Map API.
    Filters nodes to just those with lat/lon inside Colorado borders.
    :rtype: list[LiamCottleMeshtasticNode]
    """
    all_nodes: list[LiamCottleMeshtasticNode] = objectrest.get_object(url=LIAMCOTTLE_MESHTASTIC_URL,  # type: ignore
                                                                      model=LiamCottleMeshtasticNode,
                                                                      extract_list=True,
                                                                      sub_keys=["nodes"]
                                                                      )
    if not all_nodes:
        # We don't want to return an empty list, that would effectively erase the previous data snapshot
        # Instead, consider this run failed
        raise Exception(f"Could not load nodes from Liam Cottle's Meshtastic Map")

    print(
        f"Found {len(all_nodes)} nodes from MeshMap, filtering to find those with lat/lon inside Colorado")

    # Rough filter to only nodes in Colorado + padding, to cut down on number of nodes
    # that will do exact polygon math
    # This rapidly brings it down from global nodes to those that might ACTUALLY be in Colorado
    lat_min = 36
    lat_max = 41.5
    lon_min = -110
    lon_max = -101
    print(
        f"Applying pre-filter to nodes with lat between {lat_min} and {lat_max} and lon between {lon_min} and {lon_max}")
    prefiltered_nodes: list[LiamCottleMeshtasticNode] = [
        node for node in all_nodes if (
                all([node.real_latitude, node.real_longitude]) and
                all([(lat_min <= node.real_latitude <= lat_max), (lon_min <= node.real_longitude <= lon_max)])
        )
    ]

    print(
        f"Checking remaining {len(prefiltered_nodes)} nodes for exact Colorado presence"
    )
    filtered_nodes: list[LiamCottleMeshtasticNode] = [
        node for node in prefiltered_nodes if _liam_cottle_node_in_colorado(node=node)
    ]

    print(f"Found {len(filtered_nodes)} nodes in Colorado via Liam Cottle's Meshtastic Map")
    return filtered_nodes


### MeshView-specific models for parsing API responses
class MeshViewNode(BaseModel):
    id: str = Field(alias="id")
    node_id: int = Field(alias="node_id")
    long_name: str = Field(alias="long_name")
    short_name: str = Field(alias="short_name")
    hardware_model: Optional[str] = Field(alias="hw_model", default=None)
    firmware: Optional[str] = Field(alias="firmware", default=None)
    role: str = Field(alias="role")
    latitude: Optional[float] = Field(alias="last_lat", default=None)
    longitude: Optional[float] = Field(alias="last_long", default=None)
    first_seen: int = Field(alias="first_seen_us")  # UNIX timestamp
    last_seen: int = Field(alias="last_seen_us")  # UNIX timestamp

    @property
    def real_latitude(self) -> Optional[float]:
        # Move decimal seven digits to the left
        return (float(self.latitude) / 10_000_000) if self.latitude else None

    @property
    def real_longitude(self) -> Optional[float]:
        return (float(self.longitude) / 10_000_000) if self.longitude else None

    @property
    def node_role(self) -> NodeRole:
        return NodeRole.from_name(name=self.role) if self.role is not None else NodeRole.UNKNOWN

    def to_node(self) -> Node:
        return Node(
            id=self.node_id,
            long_name=self.long_name,
            short_name=self.short_name,
            hardware_model=self.hardware_model,
            role=self.node_role,
            latitude=self.real_latitude,
            longitude=self.real_longitude,
            altitude=None,
            precision=None,
        )


def _get_meshview_nodes() -> list[MeshViewNode]:
    """
    Fetch all nodes from the MeshView API.
    :rtype: list[MeshViewNode]
    """
    all_nodes: list[MeshViewNode] = objectrest.get_object(url=CM_MESHVIEW_URL,  # type: ignore
                                                          model=MeshViewNode,
                                                          extract_list=True,
                                                          sub_keys=["nodes"]
                                                          )

    if not all_nodes:
        # We don't want to return an empty list, that would effectively erase the previous data snapshot
        # Instead, consider this run failed
        raise Exception(f"Could not load nodes from MeshView")

    print(f"Found {len(all_nodes)} nodes in Colorado via MeshView")
    return all_nodes


def get_colorado_nodes() -> list[Node]:
    """
    Get all nodes in Colorado.
    :return: A list of Node objects representing all nodes in Colorado.
    :rtype: list[Node]
    """
    liam_cottle_nodes: list[LiamCottleMeshtasticNode] = _get_liam_cottle_nodes()
    liam_cottle_nodes_converted: list[Node] = [
        node.to_node() for node in liam_cottle_nodes
    ]

    meshmap_nodes: list[MeshMapNode] = _get_meshmap_nodes()
    meshmap_nodes_converted: list[Node] = [
        node.to_node() for node in meshmap_nodes
    ]

    meshview_nodes: list[MeshViewNode] = _get_meshview_nodes()
    meshview_nodes_converted: list[Node] = [
        node.to_node() for node in meshview_nodes
    ]

    # Remove duplicates by whole ID
    # Yes, it's possible two nodes, each on different maps, happen to have the same ID, but that's highly unlikely
    # Defer to the newer node if there is a conflict (list built from least-to-most trustworthy)
    unique_nodes_dict: dict[str, Node] = {}
    for node in (
            liam_cottle_nodes_converted +
            meshmap_nodes_converted +
            meshview_nodes_converted
    ):
        node_id = str(node.id)

        unique_nodes_dict[node_id] = node

    return list(unique_nodes_dict.values())


def _read_nodes_from_file(file_path: str) -> list[Node]:
    nodes = []
    if not os.path.exists(file_path):
        return nodes

    with open(file_path, "r", encoding="utf-8") as f:
        _data = json.load(f)
        for item in _data:
            nodes.append(
                Node(**item)
            )
    return nodes


def _filter_diff_nodes(existing_nodes: list[Node], new_nodes: list[Node]) -> tuple[list[Node], list[Node], list[Node]]:
    """
    Filter nodes into three categories:
    1) New nodes that are in new_nodes but not in existing_nodes
    2) Duplicate nodes that are in both existing_nodes and new_nodes
    3) Missing nodes that are in existing_nodes and not in new_nodes (potentially removed nodes)
    :param existing_nodes: The list of existing nodes to compare against.
    :param new_nodes: The list of new nodes to compare with existing nodes.
    :return: A tuple containing three lists: (new_nodes_list, duplicate_nodes_list, missing_nodes_list)
    """
    all_nodes = {}

    existing_node_hash_map = {}
    new_node_hash_map = {}

    # Loop through the "existing" nodes to build a map of hashes of their identifiers
    # and store all nodes in a combined map for easy lookup
    for node in existing_nodes:
        _hash = node.to_human_hash()
        existing_node_hash_map[_hash] = _hash
        all_nodes[_hash] = node

    # Loop through the "new" nodes to build a map of hashes of their identifiers
    # and store all nodes in a combined map for easy lookup
    for node in new_nodes:
        _hash = node.to_human_hash()
        new_node_hash_map[_hash] = _hash
        all_nodes[_hash] = node

    # Prepare sets
    existing_nodes_set = set(existing_node_hash_map.items())
    new_nodes_set = set(new_node_hash_map.items())

    true_new_nodes = new_nodes_set - existing_nodes_set
    duplicate_nodes = new_nodes_set & existing_nodes_set
    missing_nodes = existing_nodes_set - new_nodes_set

    # Look up the actual Node objects for each category based on the hashes and return them as lists
    return (
        list(all_nodes[_hash] for _hash, _ in true_new_nodes),
        list(all_nodes[_hash] for _hash, _ in duplicate_nodes),
        list(all_nodes[_hash] for _hash, _ in missing_nodes),
    )


def sync_nodes(storage_file_path: str) -> None:
    print(f"Fetching Colorado nodes...")
    nodes: list[Node] = get_colorado_nodes()
    print(f"Found {len(nodes)} nodes")

    existing_nodes: list[Node] = _read_nodes_from_file(file_path=storage_file_path)
    print(f"Loaded {len(existing_nodes)} known nodes from cache")

    print(f"Coalescing data...")
    new, duplicate, missing = _filter_diff_nodes(existing_nodes=existing_nodes, new_nodes=nodes)
    print(
        f"Found {len(new)} new nodes, {len(duplicate)} duplicate nodes, and {len(missing)} missing nodes compared to cache")

    if new or missing:
        # Write ALL nodes to file
        print("Updating cache with new nodes...")
        with open(storage_file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps([node.to_json() for node in nodes], ensure_ascii=False, indent=2))
        print("Cache updated.")
    else:
        print("No changes detected, cache not updated.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cache Meshtastic devices in Colorado.")
    parser.add_argument(
        "--nodes-data-file",
        type=str,
        help="Path to the data file to store repeater information.",
        required=True
    )
    args = parser.parse_args()

    data_file = args.nodes_data_file

    print("Syncing nodes...")
    sync_nodes(storage_file_path=data_file)
