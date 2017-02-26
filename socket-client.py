# -*- coding: utf-8 -*-
# 建立socket客户端

import socket
import sys
import random
import string

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('client socket created')

host = socket.gethostname()
port = int(''.join(random.sample(string.digits, 4)))

c.bind((host, port))
print('client bind to:%s, %s' % (host, port))

try:
    c.connect((host, 5379))
except socket.error as msg:
    cprint(msg)
    sys.close()
print('connect success, from server:', c.getpeername(), 'to client:', c.getsockname())

while True:
    msg = input('>  ')
    c.sendall(msg.encode('utf-8'))
    data = c.recv(1024)
    print(data.decode())

c.close()
