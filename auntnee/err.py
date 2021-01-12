import sys, json
def not_path():
    print("Failed to solve json file")
    print("Please enter the route to json file unencrypted", end="")
    path = input(": ")
    d = json.load(open(f"{sys.path[-1]}/config.json"))
    d['path'] = path
