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
