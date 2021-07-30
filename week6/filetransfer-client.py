#!/usr/bin/env python3

import socket
fileA = open('fileA.txt','r')
RHOST = '127.0.0.1'
RPORT = 5001
SND_DATA = fileA.read()
RCV_DATA = ''

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5
C_SOCK.settimeout(timeout)

try:
    C_SOCK.connect((RHOST, RPORT))
    C_SOCK.send(bytearray(SND_DATA,'utf8'))
    print('File sent')
    RCV_DATA = C_SOCK.recv(1024)
    print(RCV_DATA.decode())
except socket.error as e:
    print(f'Connection status: {RHOST}:{RPORT} is {e}')

C_SOCK.close()