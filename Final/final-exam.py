#!/usr/bin/env python3

import sys, requests, json, argparse, bs4, socket

from requests.models import Response

parser = argparse.ArgumentParser(description='Creating a parser to add arguments')
parser.add_argument('-ip', dest='varIP', required=True, type=str, help='Enter an IP address')
parser.add_argument('-f', dest='varInt', required=True, type=int, help='Enter an integer')
url = f"http://{parser.parse_args().varIP}/q{parser.parse_args().varInt}"
print("Name: Jesse McNaught")
print(url)
myHeader = {"content-type":"text"}

def get_response():
    response = requests.get(url)
    return response.text

def parse_string():
    response = requests.get(url)
    mySoup = bs4.BeautifulSoup(response.text, features='html.parser')
    myElem = mySoup.select('H3')
    for message in myElem[0]:
        return message

def parse_header():
    response = requests.get(url, headers=myHeader)
    for key, value in response.headers.items():
        if key == 'MATC-HEADER':
            return value

def parse_json():
    response = requests.get(url)
    myDict = json.loads(response.text)
    for key in myDict.keys():
        if 'Music And Books' in myDict.keys():
            for subkey in myDict[key]:
                if '1984' in subkey.values():
                    for author in subkey.values():
                        return author
        

def socket_client():
    RHOST = parser.parse_args().varIP
    RPORTS = range(5000,6000)
    SND_DATA = b'secret'
    RCV_DATA = ''
    timeout = 50
    for RPORT in RPORTS:
        C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        C_SOCK.settimeout(timeout)
        try:
            C_SOCK.connect((RHOST, RPORT))
            C_SOCK.send(SND_DATA)
            RCV_DATA = C_SOCK.recv(1024)
            return RCV_DATA.decode()
        except socket.error as e:
            C_SOCK.close()

if parser.parse_args().varInt == 1:
    var1 = get_response()
    print(f'ANSWER: {var1}')
elif parser.parse_args().varInt == 2:
    var2 = parse_string()
    print(f'ANSWER:{var2}')
elif parser.parse_args().varInt == 3:
    var3 = parse_header()
    print(f'ANSWER:{var3}')
elif parser.parse_args().varInt == 4:
    var4 = parse_json()
    print(f'ANSWER:{var4}')
elif parser.parse_args().varInt == 5:
    var5 = socket_client()
    print(f'ANSWER:{var5}')