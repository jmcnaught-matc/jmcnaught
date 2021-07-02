#!/usr/bin/env python3

varString = "Here is a nice string to slice"
varList = ["Here","is","a","nice","list","to","slice"]

print(f"{varString[3::]}")
print(f"{varString[:3:]}")
print(f"{varString[3:12:]}")
print(f"{varString[::2]}")
print(f"{varString[::-1]}")

print(f"{varList[::-1]}")
print(f"{varList[2::-1]}")
print(f"{varList[2:4:]}")
print(f"{varList[::3]}")
print(f"{varList[1::]}")

for a in varString:
    print(a)

for a in varList:
    print(a)