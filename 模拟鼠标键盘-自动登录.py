# -*- coding: utf-8 -*-
# 模拟操作鼠标键盘，自动登录网站账号，这里以船讯网为例
# 需安装第三方库：pyautogui
# python3可用！

import pyautogui as gui, webbrowser as bro
from time import sleep

# 打开登录页面
print('\n\n 自动登录船讯网\n\n 不要动键盘鼠标！\n\n 现在开始.....')
bro.open('http://www.shipxy.com/Home/Login/')
sleep(10)

username = 'username'
password = 'password'

# 通过操作键盘自动找准输入框，并调整输入法为英文，然后输入账号密码
gui.typewrite(['tab'] * 10)
gui.typewrite(['shiftleft'])
gui.typewrite(username)
gui.typewrite(['tab'])
gui.typewrite(password)
gui.typewrite(['enter'])

input('')
