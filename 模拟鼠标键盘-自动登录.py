# -*- coding: utf-8 -*-
# 模拟操作鼠标键盘，自动登录网站账号，这里以船讯网为例
# 需安装第三方库：pyautogui, pyperclip
# python3可用！

import pyautogui as gui, webbrowser as bro, pyperclip
from time import sleep

# 打开登录页面
print('\n\n     船讯网\n\n')
ship_name = input('请输入要查找的船名（中英文均可）或IMO号，按回车键确认：\n\n>>> ')
print('\n\n现在开始自动登录和查询船舶资料\n\n 不要动键盘鼠标！')
sleep(3)
bro.open('http://www.shipxy.com/Home/Login/')
sleep(8)

# 定义复制粘贴函数，实现自动输入汉字
def paste(word):
    pyperclip.copy(word)
    gui.hotkey('ctrl', 'v')
    
gui.click(x = 579, y = 6)
# 点击账户输入框
gui.click(x = 584, y = 267)

username = 'username'
password = 'password'

# 通过操作键盘自动找准输入框，输入账号密码
sleep(1)
paste(username)
gui.typewrite(['tab'])
paste(password)
gui.typewrite(['enter'])
sleep(8)

# 自动查询用户输入的船名或IMO号
gui.click(x = 126, y = 203)
paste(ship_name)
gui.typewrite(['enter'])

input('')
