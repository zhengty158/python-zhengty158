# 也算是一个简单的运维脚本
import os, webbrowser, time, re, urllib.request as req, random

print('\n\n        法律事务管理信息系统检测工具\n\n')

# 首先测试服务器是否正常运行
print('1、测试法律系统服务器是否正常，请稍等......\n')
ping = os.popen('ping 138.16.0.88')
ping_result = ping.readlines()
keyword_1 = '平均 = (\d+)ms|Average = (\d+)ms'
keyword_2 = '(\d+)% 丢失|(\d+)% loss'
ping_time_loss = []

# 从ping命令结果列表中，提取平均连接速度和丢包率
for n in range(len(ping_result)):
    ping_time = re.findall(keyword_1, ping_result[n])
    if ping_time != []:
        ping_time_loss.append(ping_time[0][0] or ping_time[0][1])
    ping_loss = re.findall(keyword_2, ping_result[n])
    if ping_loss != []:
        ping_time_loss.append(ping_loss[0][0] or ping_loss[0][1])
print('法律系统服务器，本次连接时间为{time}毫秒（平均），数据包丢失率为{loss}%（平均）'.format(time = ping_time_loss[1], loss = ping_time_loss[0]))
time.sleep(random.randint(1, 4))
if ping_time_loss == ['0', '0']:
    print('\n测试结果：与服务器连接正常，服务器运行正常\n\n')
    # 正常情况下，公司内部局域网连接速度为0ms，丢包率为0%
else:
    print('\n测试结果：与服务器连接异常，服务器可能未正常运行，应联系科技部同事处理\n\n')
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
    print('测试结果：法律系统首页异常（无法显示）\n\n------------------------------------------------\n\n测试结束，法律系统不能正常使用\n\n现在打开服务器管理系统，可在此重启法律系统服务器.....')
    time.sleep(random.randint(5, 10))
    # 如果以上测试异常，就进入服务器管理系统重启法律系统服务器
    webbrowser.open('https://10.10.254.10/index')
    input('')
