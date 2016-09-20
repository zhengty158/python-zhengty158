# -*- coding: utf-8 -*-

import random
secret = random.randint(0,9)
temp = input('猜猜我现在心里想的是哪个数字:')
guess = int(temp)
while guess != secret:
	temp = input('猜错了，再来一次：')
	guess = int(temp)
	if guess == secret:
		print('卧槽，愚蠢的人类居然猜中了')
		print('嘿嘿，猜中了也没奖励')
	else:
		if guess < secret:
			print('不好意思，小了！')
		else:
			print('大了大了，再猜再猜')
print('猜中了，游戏结束')