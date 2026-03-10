def blacklisted_emojis() -> list[str]:
    """
    Get a list of blacklisted emojis that should not be used in ColoradoMesh.
    :return: A list of blacklisted emojis that should not be used in ColoradoMesh.
    :rtype: list[str]
    """
    return [
        "🖕",  # Middle Finger
        "🖕🏻",  # Middle Finger: Light Skin Tone
        "🖕🏼",  # Middle Finger: Medium-Light Skin Tone
        "🖕🏽",  # Middle Finger: Medium Skin Tone
        "🖕🏾",  # Middle Finger: Medium-Dark Skin Tone
        "🖕🏿",  # Middle Finger: Dark Skin Tone
        "🤖",  # Robot Face (reserved for bots)
    ]
