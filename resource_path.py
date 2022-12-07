# This is used to import assets while ensuring compatability with pyinstaller (for compiling)
# Code was ripped from https://stackoverflow.com/questions/54210392/how-can-i-convert-pygame-to-exe

import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)