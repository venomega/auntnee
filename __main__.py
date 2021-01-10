# import pyotp
try:
    import pyotp
except :
    print("Failed to find pyotp lib.\n")
    print("Please run python -m pip install pyotp\n")
    exit(1)

import curses
import jfile
import time
z = jfile.get()


def scr(stdscr):
    stdscr.addstr(0, 0, "Hello")
    stdscr.refresh()
    time.sleep(7)


curses.wrapper(scr)
