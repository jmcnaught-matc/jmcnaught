#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser(description="This is Jesse's script")

parser.add_argument('-m', dest='myText', metavar='BASIC', help='Enter some text')
parser.add_argument('-i', '--integer', dest='myInt', type=int, metavar='[an integer]', required=True, help='Enter a simple Integer')
parser.add_argument('-d', '--float', dest='myFloat', metavar='[a float]', type=float, help='Enter a simple float')
parser.add_argument('-s', '--string', dest='myString', type=str, metavar='[a string]', help='Enter a simple string')
parser.add_argument('-l', dest='myStrings', metavar='[strings] [[strings]...]', help='Enter a list of strings (space delimited)')
parser.add_argument('-t', '--set-true', metavar='', default=False, help='Toggle from default False to True')
parser.add_argument('-f', '--setfalse', metavar='', default=True, help='Toggle from default True to False')
parser.add_argument('-v', '--version', metavar='', help='show programs version number and exit')

if(len(sys.argv) == 1):
    parser.print_help()
else:
    args = parser.parse_args()
    print(f"My integer is {args.myInt}")
    print(f"My string is {args.myString}")
    print(f"My float is {args.myFloat}")
    print(f"My list is {args.myStrings}")