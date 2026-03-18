import objectrest

from coloradomesh.meshcore.models.general.node import Node
from coloradomesh.meshcore.services.public_keys import compare_public_key_ids

COLORADO_NODE_DATA = "https://raw.githubusercontent.com/Colorado-Mesh/coloradomesh_python/refs/heads/master/data/meshcore/nodes/nodes.json"


def get_colorado_nodes() -> list[Node]:
    """
    Get all nodes in Colorado via the ColoradoMesh MeshCore node snapshot.
    :return: A list of Node objects representing all repeaters/room servers in the Denver region.
    :rtype: list[Node]
    """
    nodes: list[Node] = objectrest.get_object(url=COLORADO_NODE_DATA,  # type: ignore
                                              model=Node,
                                              extract_list=True)
    return nodes


def get_conflicting_nodes(public_key_id: str) -> list[Node]:
    """
    Get all nodes that conflict with the provided public key ID.
    :return: A list of Node objects representing all nodes that conflict with the provided public key ID.
    :rtype: list[Node]
    """
    repeaters: list[Node] = get_colorado_nodes()
    return [repeater for repeater in repeaters if
            compare_public_key_ids(id_1=repeater.public_key_id, id_2=public_key_id)]
