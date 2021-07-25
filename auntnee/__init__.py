"""
for now do nothing
"""
import sys
import os
import json

sys.path.append(__file__[:-11])


try:  # for check json file before curses init
    open(f"{os.environ['HOME']}/.auntnee.conf")
except:
    import err
    err.not_path()
    exit(0)

try:
    open(json.load(open(f"{os.environ['HOME']}/.auntnee.conf"))['path']).close()
except:
    print ("Can not access json file, Has the json file been moved/removed?")
    err.not_path()
    exit(0)

