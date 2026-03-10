from coloradomesh.meshcore.models.general.node import Node


def compare_public_key_ids(id_1: str, id_2: str) -> bool:
    """
    Compare two public key IDs (the first byte of the public key) to determine if they conflict.
    Two public key IDs conflict if they are the same (case-insensitive).
    :param id_1: The first public key ID to compare.
    :type id_1: str
    :param id_2: The second public key ID to compare.
    :type id_2: str
    :return: True if the public key IDs conflict, False otherwise.
    :rtype: bool
    """
    return id_1.upper() == id_2.upper()


def id_exists_in_list(id_: str, ids_to_track: list[str]) -> bool:
    """
    Check if a public key ID exists in a list of public key IDs (case-insensitive).
    :param id_: The public key ID to check for existence in the list.
    :type id_: str
    :param ids_to_track: The list of public key IDs to check against.
    :type ids_to_track: list[str]
    :return: True if the public key ID exists in the list, False otherwise.
    :rtype: bool
    """
    return any(compare_public_key_ids(id_1=id_, id_2=existing_id) for existing_id in ids_to_track)


def _find_unused_public_key_id_by_two_chars(nodes: list[Node]) -> str:
    """
    Find a public key ID in a list of nodes by comparing the first two characters (the first byte) of the public key.

    This is a temporary patch that will return XX00 for any public key, until MeshCore officially supports the full 4-character public key ID.
    """
    used_public_key_ids: set[str] = set(node.public_key_id_2_char for node in nodes)

    for i in range(256):
        public_key_id = f"{i:02x}"
        if is_reserved_public_key_id(public_key_id):
            continue
        if not id_exists_in_list(id_=public_key_id, ids_to_track=list(used_public_key_ids)):
            return f"{public_key_id}00"

    raise RuntimeError("No available public key IDs found")


def _find_unused_public_key_id_by_four_chars(nodes: list[Node]) -> str:
    """
    Find a public key ID in a list of nodes by comparing the first four characters (the first two bytes) of the public key.
    This is the intended implementation once MeshCore officially supports the full 4-character public key ID.
    """
    used_public_key_ids: set[str] = set(node.public_key_id_4_char for node in nodes)

    for i in range(0x0000, 0x10000):
        public_key_id = f"{i:04x}"
        if is_reserved_public_key_id(public_key_id):
            continue
        if not id_exists_in_list(id_=public_key_id, ids_to_track=list(used_public_key_ids)):
            return public_key_id

    raise RuntimeError("No available public key IDs found")


def public_key_to_public_key_id(public_key: str) -> str:
    """
    Convert a full public key to its corresponding public key ID (the first two bytes as a hex string).
    :param public_key: The full public key to convert.
    :type public_key: str
    :return: The corresponding public key ID (the first byte as a hex string).
    :rtype: str
    """
    return public_key[:4]


def is_reserved_public_key_id(public_key_id: str) -> bool:
    """
    Check if a public key ID is reserved.
    :param public_key_id: The public key ID to check (2 or 4 hex characters).
    :type public_key_id: str
    :return: True if the public key ID is reserved, False otherwise.
    :rtype: bool
    """
    return public_key_id[:2].upper() in reserved_public_key_ids()


def reserved_public_key_ids() -> list[str]:
    """
    Get a list of all reserved public key IDs.
    :return: A list of all reserved public key IDs (2-character hex strings).
    :rtype: list[str]
    """
    reserved_ids = []

    # Add 00 and FF (reserved by LetsMesh/MeshMapper)
    reserved_ids.extend(["00", "FF"])

    # Add A-block (reserved by ColoradoMesh for future use), ref: https://ottawamesh.ca/deployment/repeaters-intercity/
    reserved_ids.extend([f"A{i:01X}" for i in range(16)])

    return reserved_ids


def find_free_public_key_id(existing_nodes: list[Node]) -> str:
    """
    Find an available public key ID that is not currently in use.

    NOTE: Public key IDs should be unique across all nodes in the network (repeaters/rooms + companions).
    Please ensure that the provided list of existing nodes includes all nodes in the network.
    :param existing_nodes: A list of existing Node objects to check for used public key IDs.
    :return: A suggested public key ID that is not currently in use.
    :rtype: str
    """
    # Iterate through all possible public key IDs and return the first one that is not in use
    return _find_unused_public_key_id_by_two_chars(nodes=existing_nodes)
