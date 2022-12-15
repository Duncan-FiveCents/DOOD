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

# Yes, I actually had to use this
# I hope you're proud of me Mr. Zhang
def quickSort(LIST,FIRST_INDEX,LAST_INDEX):
    if FIRST_INDEX < LAST_INDEX: # Tests that the list is one or more
        PIVOT = LIST[FIRST_INDEX][0]
        LEFT_INDEX = FIRST_INDEX + 1
        RIGHT_INDEX = LAST_INDEX

        DONE = False
        while not DONE:
            while LEFT_INDEX <= RIGHT_INDEX and LIST[LEFT_INDEX][0] <= PIVOT:
                LEFT_INDEX += 1
            while RIGHT_INDEX >= LEFT_INDEX and LIST[RIGHT_INDEX][0] >= PIVOT:
                RIGHT_INDEX -= 1
            
            if RIGHT_INDEX < LEFT_INDEX:
                DONE = True
            else:
                TEMP = LIST[LEFT_INDEX][0]
                LIST[LEFT_INDEX][0] = LIST[RIGHT_INDEX][0]
                LIST[RIGHT_INDEX][0] = TEMP

        TEMP = LIST[FIRST_INDEX][0]
        LIST[FIRST_INDEX][0] = LIST[RIGHT_INDEX][0]
        LIST[RIGHT_INDEX][0] = TEMP

        quickSort(LIST,FIRST_INDEX,RIGHT_INDEX-1)
        quickSort(LIST,RIGHT_INDEX+1,LAST_INDEX)
        return LIST