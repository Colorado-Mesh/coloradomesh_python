import objectrest

from denvermesh.meshcore.models.general.node import Node
from denvermesh.meshcore.services.public_keys import compare_public_key_ids

DENVER_REPEATERS_DATA = "https://raw.githubusercontent.com/Denver-Mesh/docs/refs/heads/master/MeshCore/nodes/repeaters.json"


def get_denver_repeaters() -> list[Node]:
    """
    Get all repeaters/room servers in the Denver region from the MeshMapper snapshot.
    :return: A list of Node objects representing all repeaters/room servers in the Denver region.
    :rtype: list[Node]
    """
    nodes: list[Node] = objectrest.get_object(url=DENVER_REPEATERS_DATA,  # type: ignore
                                              model=Node,
                                              extract_list=True)
    return nodes


def get_conflicting_repeaters(public_key_id: str) -> list[Node]:
    """
    Get all repeaters/room servers that conflict with the provided public key ID.
    :return: A list of Node objects representing all repeaters/room servers that conflict with the provided public key ID.
    :rtype: list[Node]
    """
    repeaters: list[Node] = get_denver_repeaters()
    return [repeater for repeater in repeaters if
            compare_public_key_ids(id_1=repeater.public_key_id, id_2=public_key_id)]
