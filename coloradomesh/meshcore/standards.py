# 3-5-5-2-4 = 19 + 4 = 23
REPEATER_NAMING_SCHEMA = "{region}-{city}-{landmark}-{type}-{pub_key_id}"  # Ex. DEN-DENVR-CHSMN-RC-XXXX for a core repeater near Chessman Park in Denver, Colorado
# 3-11-2-4 = 20 + 3 = 23
REPEATER_NAMING_SCHEMA_ALT = "{region}-{landmark}-{type}-{pub_key_id}"  # Ex. COS-PIKESPEAK-RC-XXXX for a core repeater on Pikes Peak, which is not within a city

# 4 10 4 = 18 + 3 = 23
COMPANION_NAMING_SCHEMA_PKID = "{emoji}{handle} {public_key_id}"  # Ex. 🔥Alice XXXX for a companion device owned by Alice
# 4 10 4 = 18 + 3 = 23
COMPANION_NAMING_SCHEMA_COUNTER = "{emoji}{handle} MY{counter}"  # Ex. 🔥Alice MY01 for the primary companion device owned by Alice
# ^ M and Y are not a valid hex character, so it shouldn't be confused with a public key
# 4 10 4 = 18 + 3 = 23
COMPANION_NAMING_SCHEMA_ROLE = "{emoji}{handle} {role}"  # Ex. 🔥Alice PRIM for the primary companion device owned by Alice

DEFAULT_REPEATER_SETTINGS = {
    'txdelay': 0.5,
    'direct.txdelay': 0.2,
    'rxdelay': 0,
    'advert.interval': 240,
    'flood.advert.interval': 24,
    'guest.password': "",
    'prefix_size': 2
}

REPEATER_SETTINGS_HILLTOP = {
    'txdelay': 2.0,
    'direct.txdelay': 2.0,
    'rxdelay': 3.0,
    # Core repeaters are 3-byte prefixes by default to better ensure uniqueness across multi-region/multi-state network
    'prefix_size': 3
}
REPEATER_SETTINGS_FOOTHILLS = {
    'txdelay': 1.5,
    'direct.txdelay': 1.0,
    'rxdelay': 3.0
}
REPEATER_SETTINGS_SUBURBAN = {
    'txdelay': 0.8,
    'direct.txdelay': 0.4,
    'rxdelay': 3.0
}
REPEATER_SETTINGS_LOCAL = {
    'txdelay': 0.3,
    'direct.txdelay': 0.1,
    'rxdelay': 3.0
}
REPEATER_SETTINGS_MOBILE = {
    'txdelay': 3.0,
    'direct.txdelay': 2.5,
    'rxdelay': 3.0
}

PUBLIC_CHANNEL_KEY = "8b3387e9c5cdea6ac9e5edbaa115cd72"  # This is publicly known (docs.meshcore.io/companion_protocol/)
COLORADOMESH_MQTT_HOST = "mqtt.meshcore.coloradomesh.org"
COLORADOMESH_MQTT_PORT = 1883
COLORADOMESH_MQTT_AUDIENCE = "mqtt.meshcore.coloradomesh.org"
