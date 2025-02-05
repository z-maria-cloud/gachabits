# Gachabits

A library of words to be used in random generators.

Gachabits contains 600+ words. By deciding how to combine these words we can generate many kinds of things, for example clothing items, characters, food, magic weapons, spells and many more.

I mainly use Gachabits to spark creative ideas on what to draw or what to write about.

## What's inside?

Gachabits is a single JSON file that sort of looks like this:

`"weapons": ["sword", "bow", "crossbow", "axe", "dagger", "wand", "staff"],
 "rarity": ["common", "uncommon", "rare", "mythic", "legendary"],
"jewelry": ["necklace", "earrings", "pendant", "bracelet", "ring", "hairpin"],`

## How can I use it?

We can programmatically choose words and combine them. For example, this simple Python snippet generates random weapons:

`
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
`

Will output results similar to these:

`
A uncommon axe that is quite dangerous
A mythic sword that is quite tiny
A common dagger that is quite awful
`
## What's included

- `gachabit.json`: contains the words
- `analysis.py`: lists the words categories and counts the total words included in the JSON file
- `example.py`: simple use case example

*more coming soon*