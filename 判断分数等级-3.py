# -*- coding: utf-8 -*-

得分 = int(input('请输入你的得分：'))
if 90 < 得分 <= 100:
	print ('优秀')
elif 80 < 得分 <= 90:
	print ('良好')
elif 60 <= 得分 <= 80:
	print ('合格')
elif 得分 < 60:
	print ('不合格')
elif 得分 > 100 or 得分 < 0:
	print ('输入错误，请重新输入')