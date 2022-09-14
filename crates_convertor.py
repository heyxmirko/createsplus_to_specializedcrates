import json
import string
from puvodni_config import puvodni_config

puvodni = json.loads(puvodni_config)
novy_list = []
novy = ""
for item in puvodni["Winnings"]:

    print("#CONVERTING ITEM ID:", item)
    path = puvodni["Winnings"][item]

    enchant = f"""{path["Enchantments"]}""".replace("-", ";")


    if path["Type"] == "COMMAND":
        novy = """
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
        novy = """
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
    novy_list.append(novy)


for x in novy_list:
    print(x)


