import json
import model

with open("poke_data.json", "r") as poke_file:
    poke_data = json.load(poke_file)
    print(poke_data)
    for poke in poke_data:
        id_ = poke["id"]
        name = poke["name"]
        type_ = poke["type"]
        height = poke["height"]
        weight = poke["weight"]
        owned_by = poke["ownedBy"]
        for owner in owned_by:
            name_o = owner["name"]
            town_o = owner["town"]

            # model.insert_poke(id_, name, type_, height, weight)
            # model.insert_ownedby(name_o, town_o)
            # model.insert_trainers(id_, name_o,town_o)

