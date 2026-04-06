import argparse
import json
import os
from typing import Optional

import objectrest
from pydantic import BaseModel

from coloradomesh.colorado import COLORADO
from coloradomesh.internal.utils import iso8601_to_unix_timestamp
from coloradomesh.meshcore.models.general import Node, NodeType
from coloradomesh.meshcore.models.general.node_params import NodeParams
from coloradomesh.meshcore.services.stats import determine_region_by_latitude_and_longitude

MESHMAPPER_REPEATERS_URL = "https://co.meshmapper.net/repeaters.json"  # Only repeaters in Colorado region
MESHCORE_MAP_URL = "https://map.meshcore.dev/api/v1/nodes"  # All MeshCore devices globally

_COLORADO = COLORADO


### MeshMapper-specific models for parsing API responses

class MeshMapperNode(BaseModel):
    id: str
    hex_id: str
    name: str
    lat: float
    lon: float
    last_heard: int  # Unix timestamp
    created_at: str  # Unix timestamp as string
    enabled: int
    power: str
    iata: str

    def to_node(self) -> Node:
        return Node(
            public_key=self.hex_id,
            name=self.name,
            node_type=NodeType.REPEATER,  # Some are rooms, but the API doesn't discern this, so we assume
            created_at=int(self.created_at) or 0,
            last_heard=self.last_heard or 0,
            owner=None,
            latitude=self.lat,
            longitude=self.lon,
            params=None,
            estimated_region_iata=determine_region_by_latitude_and_longitude(latitude=self.lat, longitude=self.lon).code
            if (self.lat and self.lon) else None,
        )


def _get_meshmapper_nodes() -> list[MeshMapperNode]:
    """
    Fetch repeaters (not companions) from the MeshMapper API for the CO region and return them as a list of MeshMapperNode objects.
    :return: A list of MeshMapperNode objects representing the repeaters in the CO region.
    :rtype: list[MeshMapperNode]
    """
    all_nodes: list[MeshMapperNode] = objectrest.get_object(  # type: ignore
        url=MESHMAPPER_REPEATERS_URL,
        model=MeshMapperNode,
        extract_list=True
    )
    print(f"Found {len(all_nodes)} repeaters in Colorado via MeshMapper API")

    return all_nodes


### MeshCore Map-specific models for parsing API responses

class MeshCoreMapNodeParams(BaseModel):
    freq: Optional[float] = None
    cr: Optional[int] = None
    sf: Optional[int] = None
    bw: Optional[float] = None


class MeshCoreMapNode(BaseModel):
    public_key: str
    type: NodeType
    adv_name: str
    last_advert: str  # ISO 8601 timestamp string, e.g. "2026-02-18T01:19:00.379Z"
    adv_lat: float
    adv_lon: float
    inserted_date: str  # ISO 8601 timestamp string, e.g. "2026-02-18T01:19:00.379Z"
    updated_date: str  # ISO 8601 timestamp string, e.g. "2026-02-18T01:19:00.379Z"
    params: Optional[MeshCoreMapNodeParams] = None
    link: str
    source: str
    inserted_by: Optional[str]
    updated_by: Optional[str]

    def to_node(self) -> Node:
        return Node(
            public_key=self.public_key,
            name=self.adv_name,
            node_type=self.type,
            created_at=iso8601_to_unix_timestamp(self.inserted_date),
            last_heard=iso8601_to_unix_timestamp(self.last_advert),
            owner=None,
            latitude=self.adv_lat,
            longitude=self.adv_lon,
            params=NodeParams(
                freq=self.params.freq,
                cr=self.params.cr,
                sf=self.params.sf,
                bw=self.params.bw,
            ) if self.params else None,
            estimated_region_iata=determine_region_by_latitude_and_longitude(latitude=self.adv_lat,
                                                                        longitude=self.adv_lon).code
            if (self.adv_lat and self.adv_lon) else None,
        )


def _node_in_colorado(node: MeshCoreMapNode) -> bool:
    """
    Return true if MeshCoreMapNode is in Colorado.
    :param node: The MeshCoreMapNode to check.
    :return: True if the node is in Colorado, False otherwise.
    """
    if not node:
        return False

    if not all([node.adv_lat, node.adv_lon]):
        return False

    return _COLORADO.coordinates_within_borders(latitude=node.adv_lat, longitude=node.adv_lon)


def _get_meshcore_map_nodes() -> list[MeshCoreMapNode]:
    """
    Fetch all nodes (repeaters + companions) from the official MeshCore map
    Filters nodes to just those with lat/lon inside Colorado borders.
    :rtype: list[MeshCoreMapNode]
    """
    all_nodes: list[MeshCoreMapNode] = objectrest.get_object(url=MESHCORE_MAP_URL,  # type: ignore
                                                             model=MeshCoreMapNode,
                                                             extract_list=True)
    print(
        f"Found {len(all_nodes)} nodes from official MeshCore map, filtering to find those with lat/lon inside Colorado")

    # Rough filter to only nodes in Colorado + padding, to cut down on number of nodes
    # that will do exact polygon math
    # This rapidly brings it down from 27,000 global nodes to the ~250 that might ACTUALLY be in Colorado
    lat_min = 36
    lat_max = 41.5
    lon_min = -110
    lon_max = -101
    print(
        f"Applying pre-filter to nodes with lat between {lat_min} and {lat_max} and lon between {lon_min} and {lon_max}")
    prefiltered_nodes: list[MeshCoreMapNode] = [
        node for node in all_nodes if all([(lat_min <= node.adv_lat <= lat_max), (lon_min <= node.adv_lon <= lon_max)])
    ]

    print(
        f"Checking remaining {len(prefiltered_nodes)} nodes for exact Colorado presence"
    )
    filtered_nodes: list[MeshCoreMapNode] = [
        node for node in prefiltered_nodes if _node_in_colorado(node=node)
    ]

    print(f"Found {len(filtered_nodes)} nodes in Colorado via official MeshCore map")
    return filtered_nodes


def get_colorado_nodes() -> list[Node]:
    """
    Get all nodes in Colorado.
    :return: A list of Node objects representing all nodes in Colorado.
    :rtype: list[Node]
    """
    meshcore_map_nodes: list[MeshCoreMapNode] = _get_meshcore_map_nodes()
    meshcore_map_nodes_converted: list[Node] = [
        node.to_node() for node in meshcore_map_nodes
    ]

    meshmapper_nodes: list[MeshMapperNode] = _get_meshmapper_nodes()
    meshmapper_nodes_converted: list[Node] = [
        node.to_node() for node in meshmapper_nodes
    ]

    # Remove duplicates by whole ID
    # Yes, it's possible two nodes, each on different maps, happen to have the same ID, but that's highly unlikely
    # Defer to the node with the more recent `last_heard` if there is a conflict
    unique_nodes_dict: dict[str, Node] = {}
    for node in (meshcore_map_nodes_converted + meshmapper_nodes_converted):
        node_id = node.public_key.upper()

        if node_id in unique_nodes_dict:
            existing_node = unique_nodes_dict[node_id]
            existing_node_last_heard = existing_node.last_heard or 0
            conflicting_node_last_heard = node.last_heard or 0
            unique_nodes_dict[
                node_id] = node if conflicting_node_last_heard > existing_node_last_heard else existing_node
        else:
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
        _hash = node.to_hash()
        existing_node_hash_map[_hash] = _hash
        all_nodes[_hash] = node

    # Loop through the "new" nodes to build a map of hashes of their identifiers
    # and store all nodes in a combined map for easy lookup
    for node in new_nodes:
        _hash = node.to_hash()
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
    parser = argparse.ArgumentParser(description="Cache MeshCore devices in Denver.")
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
