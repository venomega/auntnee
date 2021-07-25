import sys
import help


if "-h" in sys.argv or "--help" in sys.argv:
    help.help()
if "-a" in sys.argv or "--add" in sys.argv:
    import jfile
    jfile.add()
    exit(0)

try:
    import pyotp
    del pyotp
except:
    print("Failed to find pyotp lib.\n")
    print("Please run python -m pip install pyotp\n")
    exit(1)

from screen import scr
from curses import wrapper


wrapper(scr)
