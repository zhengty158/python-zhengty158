#! python2
# -*- coding: utf-8 -*-
# 模拟操作鼠标键盘，自动登录网站账号，这里以船讯网为例
# 需要安装第三方库：PyUserInput pyHook pyWin32
# 由于pyHook还不支持win7-win10平台的python3， 只能先用python2

import pymouse,pykeyboard,os,sys
from pymouse import *
from pykeyboard import PyKeyboard
import webbrowser, time

# 建立鼠标、键盘事件
m = PyMouse()
k = PyKeyboard()

# 显示提示信息、打开网站登录页面
print '自动登录船讯网\n不要动键盘鼠标！\n\n现在开始.....'
time.sleep(3)
webbrowser.open('http://www.shipxy.com/Home/Login/')
time.sleep(5)

# 通过tab键自动找到输入框，并依次输入用户名、密码
# 下面的第一个enter是为了不切换中英文输入法
k.tap_key(k.tab_key, n = 10)
time.sleep(1)
k.type_string('username')
k.tap_key(k.enter_key)
k.tap_key(k.tab_key)
k.type_string('password')
k.tap_key(k.enter_key)
