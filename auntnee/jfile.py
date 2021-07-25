import sys
import os
import random
import json
# add encryptation missing

# aegis json compatibility, missing output
version = 1
header = {"slots": None, "params": None}
db = {"version": 1, "entries": []}


def retrive_data():  # get json config
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


def generate_uuid():
    def r(x): return random.randbytes(x).hex()
    return f"{r(4)}-{r(2)}-{r(2)}-{r(2)}-{r(6)}"


def add():
    data = retrive_data()
    d = {'type': 'totp', 'uuid': '', 'name': '', 'issuer': '', 'icon': None,
         'info': {'secret': '', 'algo': 'SHA1', 'digits': 6, 'period': 30}}
    try:
        d['uuid'] = generate_uuid()
        d['issuer'] = sys.argv[2]
        d['name'] = sys.argv[3]
        d['info']['secret'] = sys.argv[4]
    except:
        print ("You must provide:\n --add <issuer> <name> <key>\n")
        exit(1)

    data["db"]['entries'].append(json.dumps(d))
    path = json.load(open(f"{os.environ['HOME']}/.auntnee.conf"))['path']
    json.dump(data, open(path,'w'))
    exit(0)
