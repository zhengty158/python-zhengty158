# coding:utf-8
# 建立socket客户端
# 能连上，但还不能交互信息

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8888

s.connect((host, port))

s.recv(1024)

s.close()
