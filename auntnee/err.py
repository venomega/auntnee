import sys
import json
import os


def not_path():
    print("Failed to solve json file")
    print("Please enter the route to json file unencrypted", end="")
    path = input(": ")
    #d = json.load(open(f"{os.environ['HOME']}/.auntnee.conf"))
    #d['path'] = path
    d = {'path': path}
    json.dump(d, open(f"{os.environ['HOME']}/.auntnee.conf", 'w'))
