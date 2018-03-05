#!/usr/bin/env python3

import json

from collections import OrderedDict

# Retrieving information

print("Server name: ", end='', flush=True)
server = input()
print("IP address: ", end='')
ip = input()
print("User informations:\nUsername: ", end='')
username = input()
print("Shell: ", end='')
sh = input()
print("ssh_key: ", end='')
sshkey = input()

# Putting information in an OrderedDict to keep the order the same. JSON does not allow you to handle ordering properly.

dic = OrderedDict()
dic['server'] = server
dic['ip'] = ip
dic['informations'] = (username, sh, sshkey)


# Dumping and printing the JSON format

print(json.dumps(dic, indent=4))

print("\nFilename you wish to save this in JSON format (.json will be appended): ", end='', flush=True)
filename = input() + '.json'

with open(filename, 'a') as filejson:
	filejson.write(json.dumps(dic, indent=4) + "\n")
