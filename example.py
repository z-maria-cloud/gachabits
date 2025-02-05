import random
import json

def r(items):
    return random.choice(items)

def simple_weapon():
    return f"A {r(gacha["rarity"])} {r(gacha["weapons"])} that is quite {r(gacha["modifiers"])}"

gacha = ""
with open('gachabits.json', 'r') as file:
	gacha = json.load(file)

print(simple_weapon())
