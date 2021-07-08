#!/usr/bin/env python3

myFile = open("/etc/passwd","r")
strfiletext = myFile.read()
print(strfiletext)
print(type(strfiletext))
print(len(strfiletext))
myFile.close()
print("Where t = number of characters in string")
print("Use this technique when you need to put the data into a string.")

myFile = open("/etc/passwd","r")
listfiletext = myFile.readlines()
print(listfiletext)
print(type(listfiletext))
print(len(listfiletext))
myFile.close()
print("Where t = number of objects in a list")
print("Use this technique when you need to put the data in a list.")

myFile = open("/etc/passwd","r")
varfiletext = myFile.read()
for line in myFile:
    print(line)
print(varfiletext)
print(type(varfiletext))
print(len(varfiletext))
myFile.close()
print("Use this technique to loop through a file.")