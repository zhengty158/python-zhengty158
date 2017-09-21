# 也算是一个简单的运维脚本
import os, webbrowser, time, re, urllib.request as req, random

print('\n\n        法律事务管理信息系统检测工具\n\n')

# 首先测试服务器是否正常运行
print('1、测试法律系统服务器是否正常，请稍等......')
url_1 = req.Request('http://138.16.0.88')
time.sleep(random.randint(1, 4))
try:
    status_code = req.urlopen(url_1).getcode()
    if status_code == 200:
        print('\n服务器当前状态代码：200')
        print('\n测试结果：与服务器连接正常，服务器运行正常\n\n')
except u_err.URLError as error:
    print('\n错误代码：', error.reason)
    print('\n测试结果：与服务器连接异常，服务器可能未正常运行，请联系科技部同事处理\n\n')

time.sleep(2)


# 然后测试法律系统首页是否正常
print('2、测试法律系统首页能否正常访问，请稍等......\n')
url = req.urlopen('http://138.16.0.88:20/')
data = url.read().decode('utf-8')

# 如果正常，网页源码能提取到“法律”，否则提取到“无法”
keyword_3 = '.*法律.*|.*无法.*'
readlist = re.findall(keyword_3, data)
if '法律' in readlist[0]:
    print('测试结果：法律系统首页正常')
    time.sleep(random.randint(1, 4))
    print('\n-------------------------------------------------')
    input('\n\n测试结束，法律系统能正常使用')
else:
    print('测试结果：法律系统首页异常（无法显示）\n\n')
    print('------------------------------------------------')
    print('\n\n测试结束，法律系统不能正常使用\n\n现在打开服务器管理系统，可在此重启法律系统服务器.....')
    time.sleep(random.randint(5, 10))
    # 如果以上测试异常，就进入服务器管理系统重启法律系统服务器和Tomcat
    webbrowser.open('https://10.10.254.10/index')
    input('')
