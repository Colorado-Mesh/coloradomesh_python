from denvermesh.meshcore.services.channels import get_hashtag_channel_keys


class TestChannels:
    def test_get_hashtag_channel_keys(self):
        channel_name = "#bot"
        expected_secret = "eb50a1bcb3e4e5d7bf69a57c9dada211"
        expected_hash = "ca"

        secret, channel_hash = get_hashtag_channel_keys(channel_name)

        assert secret == expected_secret, f"Expected secret {expected_secret}, got {secret}"
        assert channel_hash == expected_hash, f"Expected hash {expected_hash}, got {channel_hash}"
