# OBS clip namer

By fastattack, 2024, MIT license


> [!NOTE]
> The script is only working on Windows


## Introduction
This obs script organizes your replays: it names the replays by adding the game name at the start of the name of the file and it sorts the replays in folders that corresponds to the game the replay has been taken in.

The name of the files will be changed to the name of the application running in fullscreen when the replay is saved, if there is not any app running in fullscreen, the replay will be sorted in the `unknown` folder.


## Installation
1. Install python ([python download](https://www.python.org/downloads/)) and link your installation with obs ([tutorial](https://www.youtube.com/watch?v=t7RhpvlVte0)).
2. Install the required modules:
   1. Install pywin 32 by running `pip install pywin32` in your command prompt. To do so, just launch the command prompt by searching for cmd and if you have installed python (you should have already installed it at this step) just copy `pip install pywin32` in the text area and press enter.
3. Download the `clip namer.py` file.
4. Copy the `clip namer.py` in the obs scripts folder (if you installed obs without changing its path, it should be `C:\Program Files\obs-studio\data\obs-plugins\frontend-tools\scripts`).
5. Add the script in obs by clicking `tools` at the top of obs window, then press `scripts`, then in `scripts` press `+` and select the `clip namer.py` file.
6. You are done ! If you encounter a bug or have a question about how to use the script, please use the github issues tab [here](https://github.com/fastattackv/OBS-clip-namer/issues). 
