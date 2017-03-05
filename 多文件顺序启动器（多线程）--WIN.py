# -*- coding: utf-8 -*-
# 多文件顺序启动器（多线程）
# 按设定的顺序，依次打开文件，让电脑代替简单重复劳动
# 学习了thread的基础用法，让各个文件可以同时打开了
# 以下代码，以密码管理软件KeePass为例

import os
import _thread
import time

# 先打开浏览器
def bro():
    browser = '"d:\\program files (x86)\\Mozilla Firefox\\firefox.exe"'
    os.system(browser)      # 如果是单线程，浏览器打开后不关闭，程序就不会继续打开后续文件
    
# 再依次打开KeePass密码库文件
def op_kee(x, y):
    location_1 = 'd:\\KeePass-2.35-密码管理\\密码库-1.kdbx'
    location_2 = 'd:\\KeePass-2.35-密码管理\\密码库-2.kdbx'
    time.sleep(x)           # 设置打开"浏览器"之后的等待时间"x"
    os.system(location_1)
    time.sleep(y)           # 设置打开"密码库-1.kdbx"之后的等待时间"y"
    os.system(location_2)

_thread.start_new_thread(bro, ())
_thread.start_new_thread(op_kee, (5, 5))        # 参数含义为（函数名， （函数的参数1，参数2））

input('完成')
_thread.exit()
