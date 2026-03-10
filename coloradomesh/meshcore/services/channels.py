import hashlib
from typing import Tuple


def get_hashtag_channel_keys(channel_name: str) -> Tuple[str, str]:
    """
    Get the secret key and channel hash for a given hashtag channel name.
    :param channel_name: The name of the channel to get the hashtag channel key for.
    :type channel_name: str
    :return: The corresponding hashtag channel secret key and channel hash for the given channel name.
    :rtype: Tuple[str, str]
    """
    # ref: https://analyzer.letsmesh.net/channels
    # Derived from JavaScript process:
    # 1. Filter channel name: lowercase, keep only a-z, 0-9, and hyphens
    # 2. SHA256 hash the filtered name
    # 3. First 16 bytes (128 bits) = channel secret key
    # 4. SHA256 hash those 16 bytes, first byte = channel ID (hash)
    if not channel_name.startswith("#"):
        raise ValueError("Channel name must start with #")
    # ^ Doesn't really matter, because the character will be stripped out in the next step,
    # but somewhat ensures users are providing an actual #channel public channel

    if not len(channel_name) > 1:
        raise ValueError("Channel name must be at least 2 characters long (including #)")

    # Step 1: Filter channel name, allowing only lowercase letters, numbers, and hyphens, and ensuring it starts with #
    filtered_name = "#" + "".join(c for c in channel_name[1:].lower() if (c.isalnum() or c == '-'))

    # Step 2: SHA256 hash the filtered name
    name_hash = hashlib.sha256(filtered_name.encode()).digest()
    name_hash_array = bytearray(name_hash)

    # Step 3: First 16 bytes (128 bits) = channel secret key, represented as a hex string
    name_hash_first_16_bytes = name_hash_array[:16]
    channel_secret = "".join(f"{b:02x}" for b in name_hash_first_16_bytes)

    # Step 4: SHA256 hash those 16 bytes, first byte = channel ID (hash), represented as a hex string (padded)
    channel_secret_hash = hashlib.sha256(name_hash_first_16_bytes).digest()
    channel_secret_hash_array = bytearray(channel_secret_hash)
    channel_hash = f"{channel_secret_hash_array[0]:02x}"  # First byte as hex string, padded to 2 characters

    return channel_secret, channel_hash
