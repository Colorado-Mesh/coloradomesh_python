import objectrest

from coloradomesh.meshcore.models.general.companion import Companion
from coloradomesh.meshcore.models.general.node import Node
from coloradomesh.meshcore.models.general.repeater import Repeater
from coloradomesh.meshcore.models.general.room_server import RoomServer
from coloradomesh.meshcore.services.public_keys import compare_public_key_ids

COLORADO_NODE_DATA = "https://raw.githubusercontent.com/Colorado-Mesh/coloradomesh_python/refs/heads/master/data/meshcore/nodes/nodes.json"


def get_colorado_nodes() -> list[Node]:
    """
    Get all nodes in Colorado via the ColoradoMesh MeshCore node snapshot.
    :return: A list of Node objects representing all repeaters/room servers/companions in the Denver region.
    :rtype: list[Node]
    """
    nodes: list[Node] = objectrest.get_object(url=COLORADO_NODE_DATA,  # type: ignore
                                              model=Node,
                                              extract_list=True)
    return nodes


def get_colorado_repeaters() -> list[Repeater]:
    """
    Get all repeaters in Colorado via the ColoradoMesh MeshCore node snapshot.
    :return: a list of Repeater objects representing all repeaters in the ColoradoMesh network.
    :rtype: list[Repeater]
    """
    nodes: list[Node] = get_colorado_nodes()
    repeaters: list[Repeater] = [
        Repeater.from_node(node=node) for node in nodes if node.is_repeater
    ]

    return repeaters


def get_colorado_room_servers() -> list[RoomServer]:
    """
    Get all room servers in Colorado via the ColoradoMesh MeshCore node snapshot.
    :return: a list of RoomServer objects representing all room servers in the ColoradoMesh network.
    :rtype: list[RoomServer]
    """
    nodes: list[Node] = get_colorado_nodes()
    room_servers: list[RoomServer] = [
        RoomServer.from_node(node=node) for node in nodes if node.is_room_server
    ]

    return room_servers


def get_colorado_repeaters_and_rooms() -> list[Repeater]:
    """
    Get all repeaters and room servers in Colorado via the ColoradoMesh MeshCore node snapshot.
    :return: A list of Repeater and RoomServer objects representing all repeaters/room servers in the Denver region.
    :return: list[Union[Repeater,RoomServer]]
    """
    repeaters: list[Repeater] = get_colorado_repeaters()
    room_servers: list[RoomServer] = get_colorado_room_servers()

    return repeaters + room_servers


def get_colorado_companions() -> list[Companion]:
    """
    Get all companions in Colorado via the ColoradoMesh MeshCore node snapshot.
    :return: a list of Companion objects representing all room servers in the ColoradoMesh network.
    :rtype: list[Companion]
    """
    nodes: list[Node] = get_colorado_nodes()
    companions: list[Companion] = [
        Companion.from_node(node=node) for node in nodes if node.is_companion
    ]

    return companions


def get_conflicting_nodes(public_key_id: str) -> list[Node]:
    """
    Get all nodes that conflict with the provided public key ID.
    :return: A list of Node objects representing all nodes that conflict with the provided public key ID.
    :rtype: list[Node]
    """
    repeaters: list[Node] = get_colorado_nodes()
    return [repeater for repeater in repeaters if
            compare_public_key_ids(id_1=repeater.public_key_id, id_2=public_key_id)]
