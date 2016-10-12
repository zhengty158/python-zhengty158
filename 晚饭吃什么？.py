# -*- coding: utf-8 -*-
# 写这段代码是为了解决'晚饭选择困难症'

import random
print('晚饭不知道吃什么？我可以帮你选！')
temp = input('你想吃炒菜？还是快餐？\n炒菜请按1，快餐请按2：\n')

if temp == '1':
	caidan = ['炒青菜','酸菜粉丝汤','麻婆豆腐','炒土豆丝','虎皮青椒','山药炒木耳','杂豆汤','蔬果沙拉','糯米饭']
	print('好了，今晚就吃这些吧：')
	print(random.sample(caidan,1))
	print(random.sample(caidan,1))
	print(random.sample(caidan,1))
	
elif temp == '2':
	caidan = ['真功夫','肯德基','三明治','麦当劳','汉堡王','面条','饺子','牛排']
	print('嗯～我的建议是这个：')
	print(random.sample(caidan,1))