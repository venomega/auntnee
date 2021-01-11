# import pyotp
try:
    import pyotp
    del pyotp
except:
    print("Failed to find pyotp lib.\n")
    print("Please run python -m pip install pyotp\n")
    exit(1)

from curses import wrapper
from screen import scr

wrapper(scr)
