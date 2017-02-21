# -*- coding: utf-8 -*-
# x = 分子， y = 分母

def percent(x, y):
    percent = float('%.2f' % (x / y * 100))
    print(str(percent) + '%')
