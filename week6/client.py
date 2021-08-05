#!/usr/bin/env python3

import socket
RHOST = '127.0.0.1'
RPORT = 5000
SND_DATA = b'El nino'
RCV_DATA = ''

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5
C_SOCK.settimeout(timeout)

try:
    C_SOCK.connect((RHOST, RPORT))
    C_SOCK.send(SND_DATA)
    print('Yeah, we connected')
    RCV_DATA = C_SOCK.recv(1024)
    print(RCV_DATA.decode())
except socket.error as e:
    print(f'Connection status: {RHOST}:{RPORT} is {e}')

C_SOCK.close()