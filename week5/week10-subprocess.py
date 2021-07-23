#!/usr/bin/env python3

import subprocess

myProc = subprocess.run(['ps', '-axco', 'command'], stdout=subprocess.PIPE)
myProcString = myProc.stdout.decode()
myProcList = myProcString.split('\n')

for line in myProcList:
    print(line)

print(len(myProcList[1::]))