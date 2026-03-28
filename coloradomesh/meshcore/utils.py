from urllib.parse import quote


def build_meshcore_contact_url(name: str, public_key: str, node_type: int) -> str:
    encoded_name = quote(name)
    return f"meshcore://contact/add?name={encoded_name}&public_key={public_key.upper()}&type={node_type}"

def build_meshcore_channel_url(name: str, secret: str) -> str:
    encoded_name = quote(name)
    return f"meshcore://channel/add?name={encoded_name}&secret={secret}"
