# 也算是一个简单的运维脚本
# 法律事务管理信息系统检测工具
# 修改：这次的代码能在开机状态下一直运行，并只在发现异常时汇报
import os, webbrowser, time, re, urllib.request as req, random, urllib.error as u_err

def test_lawsys(loop):

    if loop == 1:
        print('\n\n        法律事务管理信息系统检测工具\n\n')

    # 首先测试服务器是否正常运行
    if loop == 1:
        print('1、测试法律系统服务器是否正常，请稍等......')
        time.sleep(random.randint(1, 4))
    url_1 = req.Request('http://138.16.0.88')
    try:
        status_code = req.urlopen(url_1).getcode()
        if status_code == 200:
            if loop == 1:
                print('\n服务器当前状态代码：200')
                print('\n测试结果：与服务器连接正常，服务器运行正常\n\n')
            elif loop == 2:
                    pass
    except u_err.URLError as error:
        if loop == 2:
            print('1、测试法律系统服务器是否正常，请稍等......')
        print('\n错误代码：', error.reason)
        print('\n测试结果：与服务器连接异常，服务器可能未正常运行，请询问企划部电脑室领导\n\n')

    time.sleep(2)

    # 然后测试法律系统首页是否正常
    if loop == 1:
        print('2、测试法律系统首页能否正常访问，请稍等......\n')
    url_2 = req.urlopen('http://138.16.0.88:20/')
    data = url_2.read().decode('utf-8')
    keyword_2 = '.*法律.*'
    readlist = re.findall(keyword_2, data)
    try:
        if loop == 1 and '法律' in readlist[0]:
            print('测试结果：法律系统首页正常')
            time.sleep(random.randint(1, 4))
            print('\n-------------------------------------------------')
            print('\n\n测试结束，法律系统能正常使用')
        elif loop == 2 and '法律' in readlist[0]:
            pass
    except:
        if loop == 2:
            print('2、测试法律系统首页能否正常访问，请稍等......\n')
        print('测试结果：法律系统首页异常（无法显示）\n\n')
        print('------------------------------------------------')
        print('\n\n测试结束，法律系统不能正常使用\n\n现在打开服务器管理系统，可在此重启法律系统服务器.....')
        time.sleep(random.randint(5, 10))
        # 如果以上测试均异常，就进入服务器管理系统重启法律系统服务器和Tomcat
        webbrowser.open('https://10.10.254.10/')
        input('')


test_lawsys(1)

while True:
    print('\n\n不要关闭本程序，它会在开机状态下持续监控法律系统运行状态\n')
    next_time = random.randint(900, 1800)
    print('下次自动测试时间为：{time}分钟后'.format(time = round(next_time / 60, 2)))
    time.sleep(next_time)
    test_lawsys(2)
