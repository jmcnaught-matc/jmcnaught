#!/usr/bin/env python3

print("Name: Jesse McNaught")

Total = 0
lineNumb = -1
with open("Midterm-if.txt","r") as myFile:
    for line in myFile:
        lineNumb += 1
        if "gmeach18@ed.gov" in line:
            Total += lineNumb
        elif "248.253.63.149" in line:
            Total += lineNumb
        elif "Whiteland" in line:
            Total += lineNumb
        elif "80.222.19.190" in line:
            Total += lineNumb
        elif "Kayley" in line:
            Total += lineNumb
        elif "dcassyqw@microsoft.com" in line:
            Total += lineNumb

print(f"The total is: {Total}")