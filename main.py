# 1. Replace example config in previous_config_in_json.py
# 2. Run main.py¨
# 3. Copy the output and convert it back to YAML here: https://www.json2yaml.com/



import json
from previous_config_in_json import previous_config

previous = json.loads(previous_config)
new_list = []
new = ""
for item in previous["Winnings"]:

    print("#CONVERTING ITEM ID:", item)
    path = previous["Winnings"][item]

    enchant = f"""{path["Enchantments"]}""".replace("-", ";")

    if path["Type"] == "COMMAND":
        new = """
            "%s": {
                "commands": "%s",
                "chance": %d,
                "rarity": "rare",
                "give-display-item": {
                    "value": false,
                    "with-lore": false,
                    "with-name": true
                },
                "display-item": {
                "material": "%s",
                "glow": false,
                "amount": %d,
                "enchantments": "%s",
                "damage": 0,
                "name": "%s",
                "lore": %s,
                "nbt-tags": "{}"
                }
            },""" % (item,
                    path["Commands"],
                    path["Percentage"],
                     path["Item Type"],
                     path["Amount"],
                     enchant,
                     path["Name"],
                      path["Lore"])


    elif path["Type"] == "ITEM":
        new = """
            "%s": {
                "chance": %d,
                "rarity": "rare",
                "give-display-item": {
                    "value": true,
                    "with-lore": false,
                    "with-name": true
                },
                "display-item": {
                "material": "%s",
                "glow": false,
                "amount": %d,
                "enchantments": "%s",
                "damage": 0,
                "name": "%s",
                "lore": %s,
                "nbt-tags": "{}"
                }
            },""" % (item,
                    path["Percentage"],
                     path["Item Type"],
                     path["Amount"],
                     enchant,
                     path["Name"],
                      path["Lore"])
        
    print(path["Type"])
    new_list.append(new)


for x in new_list:
    print(x)


