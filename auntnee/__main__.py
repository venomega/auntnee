import sys
import help
import jfile


if "-h" in sys.argv or "--help" in sys.argv:
    help.help()
    exit(0)
if "-a" in sys.argv or "--add" in sys.argv:
    jfile.add()
    exit(0)
if "-c" in sys.argv or "--change" in sys.argv:
    jfile.change()
    exit(0)
if "-d" in sys.argv or "--delete" in sys.argv:
    jfile.delete()
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
