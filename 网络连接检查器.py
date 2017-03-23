# 一个简单的网络连接检查工具

import os

output_ip = os.popen('ipconfig /all')
output_ns = os.popen('nslookup')

# 以下DNS服务器地址仅为举例，不是真实地址
# 使用前请先用系统命令行查看DNS地址，并修改以下地址
# 一般使用'nslookup'命令检查DNS即可，但是加上'ipconfig /all'应该更保险（本初学者的想法）
if '8.8.8.8' in output_ip.read():
    if 'xx1.gd.xxxxx.net' in output_ns.read():
        print('DNS服务器未被篡改')
else:
    print('DNS服务器已被篡改！！！')

# 以下使用ping命令检查网速
output_Baidu = os.popen('ping www.baidu.com')
print('\n百度连接速度：%s（平均）' % output_Baidu.readlines()[-1][-5:-1])

output_Taobao = os.popen('ping www.taobao.com')
print('\n淘宝连接速度：%s（平均）' % output_Taobao.readlines()[-1][-5:-1])

output_Tengxun = os.popen('ping www.qq.com')
print('\n腾讯连接速度：%s（平均）' % output_Tengxun.readlines()[-1][-5:-1])
