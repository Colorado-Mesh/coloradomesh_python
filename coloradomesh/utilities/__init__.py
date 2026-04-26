def meshos_key_generator(mac_address: str) -> str:
    mac_address = mac_address.upper()
    h = ord(mac_address[0])
    for i in range(1, len(mac_address)):
        h = (h * 33 + ord(mac_address[i]))

    # "MCPP"
    xors = [0x4D, 0x43, 0x50, 0x50]

    key = ""
    for i in range(4):
        byte = ((h >> 24 - i * 8) & 0xFF) ^ xors[i]
        key += f"{byte:02x}"

    return key.upper()
