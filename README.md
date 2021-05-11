# Trails of Cold Steel 3 Modding Tools

## Introduction

A general modding tool for Trails of Cold Steel 3, also has a randomizer built in. There are 3 main parts to the program:

- Unpacker: Convert the game table files into csv and put them into their own project folder for easy organization.
- Packer: Pack a chosen project into the format the game can understand.
- Randomizer: Using a project as base, randomize the data then pack them into the format the game can understand.

## Randomizer

### Magic

(Guess characters can be optionally excluded from the randomizer)

Randomize things in the magic table of the game, which includes:

- **Crafts**: Randomize the craft set of every playable character, excluding Rean's Spirit Unification. Juna will have two craft sets, one for each of her form.
- **S-Crafts**: Randomize the S-Craft for every playable character.
- **Brave Orders**: Randomize the Brave Orders for every playable character.

## Releases

All releases of the tool can be found in the [Release Page](https://github.com/nnguyen259/ColdSteel3Tools/releases).

Additionally if you want to build the file yourself, you can use `cx_freeze` and run the command `python setup.py build`.

## Future Updates

- More features for unpacker and randomzier
- An Editor to edit the unpacked files