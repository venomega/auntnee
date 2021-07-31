import sys
import os
import ssl
import json
import template
# add encryptation missing

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
    def r(x): return ssl.RAND_bytes(x).hex()
    return f"{r(4)}-{r(2)}-{r(2)}-{r(2)}-{r(6)}"

def add():
    data = retrive_data()
    d = template.camp

    try:
        d['uuid'] = generate_uuid()
        d['issuer'] = sys.argv[2]
        d['name'] = sys.argv[3]
        d['info']['secret'] = sys.argv[4]
    except:
        print("You must provide:\n --add <issuer> <name> <key>\n")
        exit(1)

    data["db"]['entries'].append(eval(f"{d}"))
    path = json.load(open(f"{os.environ['HOME']}/.auntnee.conf"))['path']
    json.dump(data, open(path, 'w'))
    exit(0)


def change():
    data = json.load(open(f"{os.environ['HOME']}/.auntnee.conf"))
    newpath = sys.argv[2]
    try:
        open(newpath).close()
    except:
        print("Error reading file")
        exit(1)
    data['path'] = newpath
    json.dump(data, open(f"{os.environ['HOME']}/.auntnee.conf"))

def delete():
    data = retrive_data()
    count = 0
    to_delete = []
    # this have to be apart because if remove entries inside the for loop, when the list changes, the for loop breaks
    for element in data['db']['entries']:
      if element['issuer'] == sys.argv[-1]:
        count += 1
        to_delete.append(element)
    [data['db']['entries'].remove(element) for element in to_delete]
    print (f" {count} entries removed ")
    path = json.load(open(f"{os.environ['HOME']}/.auntnee.conf"))['path']
    json.dump(data, open(path,"w"))

def empty(path):
    json.dump(template.empty, open(path,'w'))
    print (f"Empty json file created on {path}")

