"""
for now do nothing
"""
import sys
import os


sys.path.append(__file__[:-11])


try:  # for check json file before curses init
    open(f"{os.environ['HOME']}/.auntnee.conf")
except:
    import err
    err.not_path()
    exit(0)
