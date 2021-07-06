#!/usr/bin/env python3

myFile = open("passwd.txt","r")
strfiletext = myFile.read()
print(strfiletext)
print(type(strfiletext))
print(len(strfiletext))
myFile.close()
print("Where t = number of characters in string")
print("Use this technique when you need to count the characters in a data string or just read the content.")

myFile = open("passwd.txt","r")
listfiletext = myFile.readlines()
print(listfiletext)
print(type(listfiletext))
print(len(listfiletext))
myFile.close()
print("Where t = number of objects in a list")
print("Use this technique when you need to count the items in a list.")

myFile = open("passwd.txt","r")
for line in myFile:
    print(line)
varfiletext = myFile.readlines()
print(len(strfiletext))
myFile.close()
print("Use this technique when you need to know the total character count and want to see each list item separately.")