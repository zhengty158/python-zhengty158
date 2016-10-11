# -*- coding: utf-8 -*-

temp = input('请输入你的得分：')
得分 = int(temp)

while 得分 > 100 or 得分 < 0:
	temp = input('输入错误，请重新输入：')
	得分 = int(temp)
if 90 < 得分 <= 100:
	print ('优秀')
elif 80 < 得分 <= 90:
	print ('良好')
elif 60 <= 得分 < 80:
	print ('合格')
else:
	print ('不合格')
print ('等级判断结束')
