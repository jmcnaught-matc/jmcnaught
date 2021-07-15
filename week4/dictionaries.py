#!/usr/bin/env python3

servers = {
    'server1.testlab.com':'192.168.1.10',
    'server2.testlab.com':'192.168.1.11',
    'server3.testlab.com':'192.168.1.12',
    'server4.testlab.com':'192.168.1.13',
    'server5.testlab.com':'192.168.1.14',
    'server6.testlab.com':'192.168.1.15'
}

print(servers.keys())
print(servers.values())
print(servers.items())

servers['server7.testlab.com'] = "192.168.1.16"
servers['server8.testlab.com'] = "192.168.1.17"

print(servers.items())

if 'server2.testlab.com' in servers.keys():
    print("Yes, server2.testlab.com exists")
else:
    print("No, server2.testlab.com does not exist")

if 'server10.testlab.com' in servers.keys():
    print("Yes, server10.testlab.com exists")
else:
    print("No, server10.testlab.com does not exist")