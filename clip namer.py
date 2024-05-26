""" Made by fastattack, 2024, MIT license
Organizes obs output directory by naming the clips and moving them in folders corresponding to the game title

Version 1.0.1
"""

import os
import shutil
import ctypes
import win32gui

import obspython as obs


GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
full_screen_rect = (0, 0, user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))


# obs funcs
def script_description():
    return "This script organize your output directory by naming the files and organizing them in the directory of the application they have been taken in\n\nMade by fastattack, 2024"


def event_dispatch(event):
    if event == obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_SAVED:
        print("Replay saved")
        replay_saved()


def script_load(settings):
    print("Loading script")
    obs.obs_frontend_add_event_callback(event_dispatch)


def script_unload():
    print("Unloading script")
    obs.obs_frontend_remove_event_callback(event_dispatch)


# script funcs
def get_fullscreen_hwnd() -> int | None:
    """ Returns the fullscreen app's hwnd, if there is no fullscreen app, returns None """
    try:
        hwnd = user32.GetForegroundWindow()
        rect = win32gui.GetWindowRect(hwnd)
        if rect == full_screen_rect:
            return hwnd
        else:
            return None
    except:
        return None


def get_window_title_from_hwnd(hwnd):
    length = GetWindowTextLength(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    GetWindowText(hwnd, buff, length + 1)
    return buff.value


def remove_forbidden_characters(text: str) -> str:
    """ Removes window forbidden characters for file names and spaces at the end of the text's """
    text = text.replace("/", "").replace("\\", "").replace(":", "").replace("*", "").replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("|", "")
    while text.endswith(" "):
        text = text.removesuffix(" ")
    return text


def replay_saved():
    """ Moves and renames a replay when it's saved to the game it has been captured in """
    hwnd = get_fullscreen_hwnd()
    if hwnd is not None:
        game = get_window_title_from_hwnd(hwnd)
        game = remove_forbidden_characters(game)
        if game == "":
            game = "unknown"
    else:
        game = "unknown"

    file_path = obs.obs_frontend_get_last_replay()
    file_directory = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)

    if not os.path.isdir(os.path.join(file_directory, game)):  # there is not already a directory for this game
        os.mkdir(os.path.join(file_directory, game))

    try:
        new_file_path = os.path.join(file_directory, game, f"{game} {file_name}")
        shutil.move(file_path, new_file_path)
        print(f"Saved replay to: {new_file_path}")
    except Exception as e:
        print(f"Unexpected error when saving replay: {e}")
