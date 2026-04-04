import binascii
import hashlib
import os
import random

from coloradomesh.meshcore.models.general.node import Node
from nacl.bindings import (
    crypto_sign_PUBLICKEYBYTES,
    crypto_sign_SECRETKEYBYTES,
)
from nacl.signing import SigningKey


class KeyGenerator:
    """
    A class for generating MeshCore public/private key pairs.
    """
    ASSUMED_RATE = 10000  # Assume 10,000 attempts per second

    def __init__(self, target_prefix: Optional[str] = None):
        self.target_prefix = target_prefix.upper() if target_prefix else None
        if self.target_prefix:
            assert all(
                c in "0123456789ABCDEF" for c in self.target_prefix), "Cannot provide non-hex characters in prefix"

    @property
    def probability(self) -> float:
        """
        Probability of any given generated public key beginning with the target prefix.
        :return: Probability of any given generated public key beginning with the target prefix.
        """
        if self.target_prefix is None:
            return 1.0

        return 1 / (16 ** len(self.target_prefix))

    @property
    def estimated_attempts(self) -> float:
        """
        Estimated number of attempts required to generate a public key beginning with the target prefix.
        :return: Estimated number of attempts, or 1 if no target prefix is set.
        """
        if not self.target_prefix:
            return 1  # Very first key should work, so effectively one attempt

        # Each hex character has 16 possibilities, so the number of attempts grows exponentially with the length of the prefix
        return 1 / self.probability

    @property
    def estimated_time(self) -> float:
        """
        Estimated time, in seconds, to generate a public key beginning with the target prefix.
        :return: Estimated time in seconds, or 0 if no target prefix is set.
        """
        if not self.target_prefix:
            return 0  # Very first key should work, so effectively zero wait

        return self.estimated_attempts / self.ASSUMED_RATE

    def generate_key_pair(self) -> tuple[str, str]:
        """
        Generate a public/private key pair where the public key starts with the target prefix (if set).
        :return: A tuple containing the generated public key and private key.
        :rtype: tuple[str, str]
        """
        return generate_public_private_key_pair_by_prefix(prefix=self.target_prefix or "")


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


def _find_next_unused_public_key_id_by_four_chars(nodes: list[Node]) -> str:
    """
    Find the very next (sequential) unused public key ID (the first two bytes as a hex string).
    :param nodes: A list of existing nodes to avoid clashing against.
    :return: The next unused public key ID (the first two bytes as a hex string).
    """
    used_public_key_ids: set[str] = set(node.public_key_id_4_char for node in nodes)

    for i in range(0x0000, 0x10000):
        public_key_id = f"{i:04x}"
        if is_reserved_public_key_id(public_key_id):
            continue
        if not id_exists_in_list(id_=public_key_id, ids_to_track=list(used_public_key_ids)):
            return public_key_id

    raise RuntimeError("No available public key IDs found")


def _attempt_find_random_unused_public_key_id_by_four_chars(nodes: list[Node], attempts: int = 10) -> str:
    """
    Find a random unused public key ID (the first two bytes as a hex string).
    :param nodes: A list of existing nodes to avoid clashing against.
    :param attempts: The number of random attempts to make before giving up.
    :return: A random unused public key ID (the first two bytes as a hex string).
    :raise Exception: If attempts exceed the maximum number of attempts.
    """
    used_public_key_ids: set[str] = set(node.public_key_id_4_char for node in nodes)

    possible_public_key_ids = range(0x0000, 0x10000)
    public_key_ids_choices = random.sample(possible_public_key_ids, attempts)

    for i in public_key_ids_choices:
        public_key_id = f"{i:04x}"
        if is_reserved_public_key_id(public_key_id):
            continue
        if not id_exists_in_list(id_=public_key_id, ids_to_track=list(used_public_key_ids)):
            return public_key_id

    raise Exception("Could not find a random unused public key ID withing the specified number of attempts")


def _find_unused_public_key_id_by_four_chars(nodes: list[Node]) -> str:
    """
    Find a public key ID in a list of nodes by comparing the first four characters (the first two bytes) of the public key.
    First attempt to find a random unused public key ID (to avoid sequential clustering).
    Fallback to using the next sequential unused public key ID if random search fails within 10 attempts.
    """
    try:
        return _attempt_find_random_unused_public_key_id_by_four_chars(nodes=nodes, attempts=10)
    except Exception:
        return _find_next_unused_public_key_id_by_four_chars(nodes=nodes)

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
    return _find_unused_public_key_id_by_four_chars(nodes=existing_nodes)


def _generate_orlp_ed25519_keypair_bytes() -> tuple[bytes, bytes]:
    """
    Returns (public_key, private_key) as raw bytes:
      - public_key: 32 bytes
      - private_key: 64 bytes (ORLP Ed25519 format: expanded_scalar || random)
    """
    # Generate 32-byte random seed
    seed = os.urandom(32)

    # Hash seed with SHA-512
    digest = hashlib.sha512(seed).digest()
    digest_bytes = bytearray(digest)

    # Clamp the scalar
    clamped = digest_bytes[:32]
    clamped[0] &= 248
    clamped[31] &= 63
    clamped[31] |= 64

    # Public key derived from seed (standard Ed25519)
    public_key = SigningKey(seed).verify_key.encode()

    # Private key is `clamped` 32 bytes + last 32-bytes of `digest_bytes`
    private_key = clamped + digest_bytes[32:64]
    # Fun fact: The back-32 bytes literally don't matter when deriving the public key from the private key

    assert len(public_key) == crypto_sign_PUBLICKEYBYTES == 32
    assert len(private_key) == crypto_sign_SECRETKEYBYTES == 64

    return public_key, private_key


def _generate_public_private_key_pair_hex() -> tuple[str, str]:
    """
    Returns (public_key, private_key) as hex strings
    :return:
    """
    def to_hex(key: bytes) -> str:
        return (binascii.hexlify(key)).decode('utf-8').upper()

    public_key, private_key = _generate_orlp_ed25519_keypair_bytes()
    return to_hex(public_key), to_hex(private_key)


def generate_public_private_key_pair_by_prefix(prefix: str) -> tuple[str, str]:
    """
    Generate a public/private key pair where the public key starts with the specified prefix.
    :param prefix: The desired prefix for the public key (<=6 hex characters, e.g. "ABCDEF").
    :return: A tuple containing the generated public key and private key.
    :rtype: tuple[str, str]
    """
    assert 0 <= len(prefix) <= 6  # Can be length zero, any key will pass
    assert all(c in "0123456789abcdefABCDEF" for c in prefix)  # Must be hex characters

    prefix = prefix.upper()

    if len(prefix) == 0:
        return _generate_public_private_key_pair_hex()

    private_key = "?"
    public_key = "?"  # A character that would not be in a valid hex string

    def match_prefix(_public_key: str) -> bool:
        return str(_public_key).startswith(prefix)

    iteration_count = 0
    while not match_prefix(_public_key=public_key):
        public_key, private_key = _generate_public_private_key_pair_hex()
        iteration_count += 1

    return public_key, private_key
