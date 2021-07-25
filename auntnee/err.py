import sys
import json
import os
import jfile

def not_path():
    print("Failed to solve json file")
    print("Please enter the route to json file unencrypted", end="")
    path = input(": ")
    d = {'path': path}
    json.dump(d, open(f"{os.environ['HOME']}/.auntnee.conf", 'w'))
    try:
        json.load(open(path))
    except:
        print ("File seems to not be an Aegis json, do you want to create an empty template [Y/n]: ",end="")
        if not "n" in input().lower():
            jfile.empty(path)
