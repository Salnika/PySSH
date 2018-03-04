#!/usr/bin/env python3

import json

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

# Dumping and printing the JSON format

print(json.dumps({'informations': {'user': username, 'shell': sh, 'ssh key': sshkey}, 'server': server, 'ip': ip}, sort_keys=True, indent=4))
