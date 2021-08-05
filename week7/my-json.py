#!/usr/bin/env python3

import sys, requests, json, argparse

parser = argparse.ArgumentParser(description='Creating a parser to add arguments')
parser.add_argument('-ip', dest='varIP', type=str, help='Enter an IP address')

url = f"http://ipinfo.io/{parser.parse_args().varIP}/json"
jsonResp = requests.get(url)
myDict = json.loads(jsonResp.text)
for key in myDict.keys():
    print(f"{key}:{myDict[key]}")