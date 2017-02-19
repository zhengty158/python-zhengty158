# coding:utf-8
# 用socket建立的在线聊天程序
# 现在的功能相当于一个抛球游戏，用户A先抛球给用户B，用户B拿到球才能抛球给用户A
# 也就是说：用户A先给用户B发消息，用户B才能给用户A发消息，而且用户B回复之后，用户A才能继续发消息

# 用户A所需代码：
import socket

socket_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                # 这里使用UDP协议
socket_in.bind((socket.gethostname(), 8888))                                # 这里的主机和端口号都是本机的，仅用于测试，实际使用时需要修改

while True:
    chatmsg = input('用户A，请输入聊天内容\n> ')
    socket_in.sendto(chatmsg.encode(), ((socket.gethostname(), 6666)))      # 发送消息
    if chatmsg == '退出':
        socket_in.close()
        break
    msg, (addr, port) = socket_in.recvfrom(100)                             # 接收消息
    if msg == '退出':
        socket_in.close()
        break
    print('\n你收到一条来自用户B的消息：\n' + msg.decode() + '\n')
    
    
# 用户B所需代码：
import socket

socket_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_in.bind((socket.gethostname(), 6666))

while True:
    msg, (addr, port) = socket_in.recvfrom(100)
    if msg == '退出':
        socket_in.close()
        break
    else:
        print('\n你收到一条来自用户A的消息：\n' + msg.decode() + '\n')

    chatmsg = input('用户B，请输入聊天内容\n> ')
    socket_in.sendto(chatmsg.encode(), ((socket.gethostname(), 8888)))
    if chatmsg == '退出':
        socket_in.close()
        break
