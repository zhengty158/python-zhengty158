# 一个简单的网络连接检查工具

import os, re

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

    
# 以下使用ping命令检查网速和丢包率
site = {'淘宝':'www.taobao.com', '腾讯':'www.qq.com', '百度':'www.baidu.com'}

for k, v in site.items():
    output = os.popen('ping {website}'.format(website = v))
    output_list = output.readlines()
    keyword_1 = '平均 = (\d+)ms|Average = (\d+)ms'
    keyword_2 = '(\d+)% 丢失|(\d+)% loss'
    final_result = []
    # 从ping命令结果列表中，提取平均连接时间和丢包率
    for n in range(len(output_list)):
        output_result_1 = re.findall(keyword_1, output_list[n])
        if output_result_1 != []:
            final_result.append(output_result_1[0][0] or output_result_1[0][1])
        output_result_2 = re.findall(keyword_2, output_list[n])
        if output_result_2 != []:
            final_result.append(output_result_2[0][0] or output_result_2[0][1])
    print('\n{website}连接速度：{time}毫秒（平均）\n丢包率：{percent}%'.format(website = k, time = final_result[1], percent = final_result[0]))

input('\n\n完成')
