import objectrest

from coloradomesh.internal import utils
from coloradomesh.meshcore.models.general.node import Node, NodeType
from coloradomesh.meshcore.models.letsmesh import LetsMeshNode

LETSMESH_NODES_URL = "https://api.letsmesh.net/api/nodes?region=DEN"  # ALL devices in Denver


# TODO: Why not use LetsMesh for all devices (repeaters and companions)? LetsMesh API blocks some requests; MeshMapper doesn't, but only provides repeaters, not companions


def get_denver_companions() -> list[Node]:
    """
    Get all companion nodes in the Denver region from the LetsMesh API.
    Filters out repeaters and room servers, only including companions,
    as the LetsMesh API does not provide a way to filter by device role in the request.
    :return: A list of Node objects representing all companions in the Denver region.
    :rtype: list[Node]
    """
    letsmesh_nodes: list[LetsMeshNode] = objectrest.get_object(url=LETSMESH_NODES_URL,  # type: ignore
                                                               model=LetsMeshNode,
                                                               extract_list=True,
                                                               sub_keys=["nodes"],
                                                               headers={
                                                                   "Host": "api.letsmesh.net",
                                                                   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0",
                                                                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                                                                   "Accept-Language": "en-US,en;q=0.9",
                                                                   "Accept-Encoding": "gzip, deflate, br, zstd",
                                                                   "Connection": "keep-alive",
                                                               })
    return [
        Node(
            public_key=node.public_key,
            name=node.name,
            node_type=NodeType.COMPANION,
            created_at=utils.iso8601_to_unix_timestamp(node.first_seen),
            last_heard=utils.iso8601_to_unix_timestamp(node.last_seen),
            owner=None,  # The LetsMesh API does not provide owner information for nodes
            latitude=node.location.latitude if node.location else None,
            longitude=node.location.longitude if node.location else None,
            is_observer=node.is_mqtt_connected,
        )
        for node in letsmesh_nodes
        if node.device_role == node.device_role.COMPANION  # Only include companions, exclude repeaters and room servers
    ]
