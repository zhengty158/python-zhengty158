# -*- coding: utf-8 -*-
# 国庆在机场看到支付宝、微信支付都有扫码支付立减活动，一时兴起想自己写一段同样的代码

# 首先引用随机函数生成立减金额
# 由于随机函数生成的金额在小数点后有很多位，必须让程序只取小数点后两位，再进行计算
import random
temp = random.uniform(1,10)
zhekou = ('%.2f' % temp)

yuanjia = input('请输入购物金额:')

zhekoujia = float(yuanjia) - float(zhekou)

print ('您本次购物享受的随机立减折扣是:',zhekou,'元')
print ('您的最终付款金额是:',zhekoujia,'元')