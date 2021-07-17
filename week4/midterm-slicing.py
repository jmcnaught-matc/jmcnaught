#!/usr/bin/env python3

print ("Name: Jesse McNaught")

with open("slicing-file.txt","r") as myFile:
    list = myFile.readlines()
    varA = list[-3]
    varB = list[2:5:]
    varC = list[-10:-16:-2]
    varD = list[10:13:]
    varE = list[-19:-22:-1]
    quote = f"{varA}{''.join(varB)}{''.join(varC)}{''.join(varD)}{''.join(varE)}"
    print(quote.replace("\n"," "))