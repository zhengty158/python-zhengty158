# -*- coding: utf-8 -*-
# 停工留薪期实发工资计算器
# 使用前需要安装business_calendar模块：https://pypi.python.org/pypi/business_calendar/

import datetime
from business_calendar import Calendar, MO, TU, WE, TH, FR

def tglxqsfgz():
    print('\n\n\n     停工留薪期实发工资计算器\n\n')
    
    # 调用business_calendar模块计算除去周末的工作日天数
    year = int(input('请输入停工留薪期开始年份(数字):\n'))
    month = int(input('请输入停工留薪期开始月份(数字):\n'))
    day1 = int(input('请输入停工留薪期开始日期(数字):\n'))
    day2 = int(input('请输入停工留薪期结束日期(数字):\n'))
    date1 = datetime.datetime(year, month, day1)
    date2 = datetime.datetime(year, month, day2)
    cal = Calendar()
    print('在{date1}至{date2}期间，除去周末的工作日天数为{busdaycount}天\n'.format(date1 = date1, date2 = date2, busdaycount = cal.busdaycount(date1, date2) + 1))
    
    # 计算实发工资
    tinggongliuxinqitianshu = int(input('请根据以上天数，核实在此期间是否有法定节日，然后输入停工留薪期天数（数字）：\n'))
    # 其实可以直接用business_calendar模块排除法定节假日和周末，但是需要事先录入法定节假日
    gongzhi = float(input('请输入该月实发工资（数字）：\n'))
    gongzuorigongzhi = tinggongliuxinqitianshu * (gongzhi / 21.75)
    print('\n停工留薪期实发工资（该月工作日部分）：{jisuanjieguo}元'.format(jisuanjieguo = float('%.2f' % gongzuorigongzhi)))
    

while True:
    tglxqsfgz()
