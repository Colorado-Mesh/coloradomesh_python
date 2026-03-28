from coloradomesh.meshcore.models.general import NodeType
from coloradomesh.meshcore.services.channels import get_hashtag_channel_keys
from coloradomesh.meshcore.standards import PUBLIC_CHANNEL_KEY
from coloradomesh.meshcore.utils import build_meshcore_channel_url, build_meshcore_contact_url


class TestChannels:
    def test_get_hashtag_channel_keys(self):
        channel_name = "#bot"
        expected_secret = "eb50a1bcb3e4e5d7bf69a57c9dada211"
        expected_hash = "ca"

        secret, channel_hash = get_hashtag_channel_keys(channel_name)

        assert secret == expected_secret, f"Expected secret {expected_secret}, got {secret}"
        assert channel_hash == expected_hash, f"Expected hash {expected_hash}, got {channel_hash}"

    def test_build_meshcore_contact_url(self):
        contact_name = "TestUser"
        contact_public_key = "abcd1234"
        node_type = NodeType.COMPANION

        contact_url = build_meshcore_contact_url(name=contact_name, public_key=contact_public_key,
                                                 node_type=node_type.value)

        assert contact_url == f"meshcore://contact/add?name=TestUser&public_key=ABCD1234&type=1"

    def test_build_meshcore_channel_url(self):
        channel_name = "Public"
        channel_secret = PUBLIC_CHANNEL_KEY

        channel_url = build_meshcore_channel_url(name=channel_name, secret=channel_secret)

        assert channel_url == f"meshcore://channel/add?name=Public&secret={PUBLIC_CHANNEL_KEY}"
