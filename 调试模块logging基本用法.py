# -*- coding: utf-8 -*-
# 以随机密码生成代码为例，演示调试模块logging的基本用法

import string, random, logging

# 停止logging：logging.disable(logging.DEBUG)
logging.basicConfig(filename = 'd:\\mylog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('程序开始运行')

def pass_generator(n):
    logging.debug('用户指定的密码位数：' + str(n))
    symbols = '!@#$%^&*()-+=[{}]:";<>\'?\\/,.'
    password = ''.join(random.sample(string.digits + string.ascii_letters + symbols, n))
    logging.debug('随机样本是：' + string.digits + string.ascii_letters + symbols)
    logging.debug('生成的密码位数：' + str(len(password)))
    logging.debug('生成的密码：' + password)
    return password

pass_generator(20)
logging.debug('程序运行结束')
