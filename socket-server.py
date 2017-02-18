# coding:utf-8
# 建立并运行socket服务器端

import socket
import sys

HOST = ''                                    # 另一种写法：HOST = socket.gethostname()，但是需要在建好socket之后才有用
PORT = 8888

s = socket.socket()                          # socket.socket()默认参数是IPV4，TCP
print('Socket created')

try:
    s.bind((HOST, PORT))                     # socket.bind()参数只有一位，所以需要用()把HOST,PORT括起来
except socket.error as msg:                  # python3此处需使用except……as……语句
    print(msg)
    sys.exit()
	
print('Socket bind complete')

s.listen(10)
print('Socket now listening')

while True:                                   # 将True替换为1也可以
    conn, addr = s.accept()

    print('已连接的客户端地址：%s，端口号：%s' % (str(addr[0]), str(addr[1])))
    print('服务器信息：%s' % str(conn))

    data = conn.recv(1024)
    reply = 'ok...' + data.decode()           # python3必须注意编码问题，此处data应从bytes转换为string
    
    conn.sendall(reply.encode('utf-8'))       # 同上
    
conn.close()
s.close()
