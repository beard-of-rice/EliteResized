# Elite Resized
A simple screenshot converter written in Python 3.

## Introduction
I spent a long time looking for a simple screenshot converter for the huge bitmap screenshots produced by Elite Dangerous. I couldn't find a suitable tool, so in December 2020, I made my own in Python. It uses Python 3.8, PyQt5 and Pillow-SIMD. I tried to create an .exe version using AutoPy2Exe, but due to my lack of knowledge, I couldn't get it to work on anything other than Windows 7. The source and dodgy executables are included for your amusement.

## Requirements
It was produced using Python 3.8, PyQt5, OrJSON and Pillow-SIMD, so you'll probably need all of them! I used Qt Designer for the GUI.

## How it works
![Elite Resized](https://i.imgur.com/yKtFiyc.png)Elite Resized uses the Elite logs to collect information about every time you've taken a screenshot in game, including the location and time. This information is then included in the name of the converter file.

Please ensure your locations are set correctly. Elite journals are always .log format. Screenshots will always be .bmp. Your save location will contain your converter files. The original .bmp copies are not altered or removed!

## How to run it
This assumes you have basic knowledge of running Python programs and installing packages (ideally using pip). I used Python 3.8, PyQt5 and Pillow-SIMD v7.0.0-post3 (more performant than vanilla Pillow). I also used OrJSON 3.4.6. I think that's everything. It may run with other (later) versions of these packages, but if all else fails this should be all you need to install.

When you're ready to convert some files, run src/Main.py (in IDLE, another IDE or from the command line), ensure your locations are set correctly, choose the file type you would like to convert to and press Convert. It may take some time to get to 100% if there are a lot of files. If you close ER at any other time, it will also stop the conversion, so don't worry about runaway background processes.

## Forking
You are welcome to fork and build on my basic code as long as you make sure the source is always available, all changes are documented and a copy of the licence ([GNU AGPLv3](https://spdx.org/licenses/AGPL-3.0-or-later.html)) is included with any forks of this software.

## Support
I am a novice Python developer and usually work with other languages, but if there are any issues with the packages etc, open an issue and I will try my best to help.