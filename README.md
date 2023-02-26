# Initial Statement
First and foremost, the _**vast**_ majority of this hack was created by [DougTheDruid](https://github.com/DougTheDruid). The emphasis on the vastness can't be overstated,
as the great majority of this project came from their framework. Any and all of the hardwork that this hack accomplishes is completely their doing.
This includes the entirety of the SDK used in generating offsets and the accompanying `offsets.jon` file, the entirety of the memory reading toolset, 
the great majority of the UI implementation produced by Pyglet, the structural integrity and project flow of the hack, and the greater majority of the
project's documentation. All I've done is simply expand upon it by adding in various modules that utilize what Doug has provided.

Doug puts strong emphasis on the fact that their framework of which this project was built from is to be used as a learning tool and I can not stress enough _**how great of a learning tool his framework truly is.**_

I _**implore**_ any and all of you reading this to _**first dive into their framework they provide.**_ The only reason this repository isn't made private is due to fork synchronization.
Should I find a clean way to make this happen, this repository will immediately be made private and your only method of getting a Python SoT ESP
will be to use framework he provides and build upon it as I have.

_**Please**_, do yourself a favor, and jump into Doug's framework rather than cut and paste what poor additions I've made.
I will not keep mine up to date with any sense of urgency alongside SoT game updates. I've tinkered with this as a learning project, 
just as Doug intended with the development of their framework, so I urge you to do the same.


[DougTheDruid (GitHub)](https://github.com/DougTheDruid)

[DougTheDruid (Forum)](https://www.unknowncheats.me/forum/members/3935541.html)

Each of the following repositories should have a helpful `readme.md` file to get started.
- [Doug's Framework](https://github.com/DougTheDruid/SoT-ESP-Framework) - The entire brain, heart and soul of this fork of the SoT Python ESP hack.
- [Doug's SDK](https://github.com/DougTheDruid/SoT-Python-Offset-Finder) - An up-to-date SDK available to the community, and a 
python file to automatically generate an offsets file based on your configuration, resulting in an `offsets.json` file the framework uses.
- [Doug's Actor Map](https://github.com/DougTheDruid/SoT-Actor-Names) - A manually-created list that maps actors raw names to more common names.
- [Forum](https://www.unknowncheats.me/forum/sea-of-thieves/453603-dougs-python-sot-emporium-esp-framework-offset-builder-sdk-mappings.html)

Other credited users in the development of this SoT Python ESP hack:
- [Gummy](https://www.unknowncheats.me/forum/members/726677.html) - Previously provided an opensource C++ version of a SoT Hack. Wouldn't have been possible without him!
- [miniman06](https://www.unknowncheats.me/forum/members/2903443.html) - Pattern recognition for automatic offset generation
- [mogistink](https://www.unknowncheats.me/forum/members/3434160.html) - Supreme helper of the community and always providing valuable feedback on changes


### Installation, Prerequisites & Execution
- Install Python 3.8+
- Install (if needed) OpenGL 3.3+
- Install the requirements found in the `requirements.txt` file
- Run `main.py`
- **Note**: this fork of the SoT Python ESP hack was built in the latest version of [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows), however your preferred IDE should suffice assuming python capabilities are available.

### ESP Features
For a general idea of what this fork offers, you can skim through the [modules package](https://github.com/Igi-Foshifo/SoT-ESP-Framework/tree/main/Modules).

More specifically, the following features are currently implemented, though to what extent may vary:
- Enemy Drops
- Enemy ESP
- Loot ESP (keys, chests, skulls, crates, etc.)
- Compass header
- Event ESP
- Storm Tracker ESP
- Crew Tracker
- Oxygen Level Tracker
- Ship ESP
- Rowboat ESP
- Shipwreck ESP