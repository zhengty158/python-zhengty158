# -*- coding: utf-8 -*-

temp = input('猜猜我现在想的是哪个数字:')
guess = int(temp)
	if guess == 8:
		print('卧槽，愚蠢的人类居然猜中了')
		print('嘿嘿，猜中了也没奖励')
	else:
		if guess > 8:
			print('大了大了')
		else:
			print('小了小了')
print('game over')