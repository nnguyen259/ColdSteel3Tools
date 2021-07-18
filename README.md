# Trails of Cold Steel 3 Modding Tools

## Introduction

A general modding tool for Trails of Cold Steel 3, also has a randomizer built in. There are 3 main parts to the program:

- Unpacker: Convert the game table files into csv and put them into their own project folder for easy organization.
- Packer: Pack a chosen project into the format the game can understand.
- Randomizer: Using a project as base, randomize the data then pack them into the format the game can understand.

## Usages

For all tools, Game Directory refers to the directory where the game launcher (`Sen3Launcher.exe`) resides in.

### Unpacker

- **Project Name**: The name of the project the files will be extracted to. All projects can be found under the `/projects` folder.

### Packer

- **Project Name**: The name of the project to get packed. `TOCS3 Vanilla` is the original version of the game.

### Randomizer

- **Base Project**: The name of the project to be used as the base for the randomizer. `BaseProject` is the original version of the game.
- **Seed**: The seed to be used in the randomizer

The result of the randomizer will be saved in the `results.txt` file.

## Using the Randomizer on yuzu

To use the randomizer with yuzu (a Nintendo Switch Emulator), you can do the following steps:

1. Open yuzu, Right-Click on the game name, and select `Open Mod Data Location`.
2. Create a new folder in the location named `Randomizer`.
3. Create a new folder inside `Randomizer` named `romfs`.
4. Use the `romfs` folder as the game directory for the randomizer.
5. Enjoy!

As I have no experience with Ryujinx or Switch homebrew, follow their instructions on how to create a LayeredFS folder for mod then use that as the game directory for the randomizer.

## Randomizer

### Enemy

Randomize enemies' base stat, stat growth, elemental/status/unbalance efficacy with the option to keep the enemies' original pretrify and deathblow efficacy.

Low roll chance will make sure that some efficacy stay low so enemies aren't weak to everything.

### Stat, Craft, Orbment Line and Model

(Guest characters can be optionally excluded from the randomizer)

Randomize Base Stat, Stat Growth, Base EP, EP Growth, Orbment Line, Craft, S-Craft, Brave Order and Character Model for all playable characters. 

## Releases

All releases of the tool can be found in the [Release Page](https://github.com/nnguyen259/ColdSteel3Tools/releases).

Additionally if you want to build the file yourself, you can use `cx_freeze` and run the command `python setup.py build`.

## Future Updates

- More features for unpacker and randomzier
- An Editor to edit the unpacked files