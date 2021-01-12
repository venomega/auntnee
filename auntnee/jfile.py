import sys
import os
# add encryptation missing

# aegis json compatibility, missing output
version = 1
header = {"slots": None, "params": None}
db = {"version": 1, "entries": []}


def retrive_data():  # get json config
    import json
    path = json.load(open(f"{os.environ['HOME']}/.auntnee.conf"))['path']
    return json.load(open(path))


def arrange_list():  # for export new dict with clean data

    d = retrive_data()
    z = {}
    for entry in d['db']['entries']:
        if entry['type'] != 'totp':
            continue
        issuer = entry['issuer']
        name = entry['name']
        secret = entry['info']['secret']
        z[issuer] = {'name': name, 'secret': secret}
    return z


def get():  # macro for get list to mem
    return arrange_list()
