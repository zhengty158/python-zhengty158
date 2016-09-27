# -*- coding: utf-8 -*-

correctanswer = '七颗龙珠'
answer = input('请回答：召唤神龙需要几颗龙珠？：')

while True:
	if answer == correctanswer:
		break
	answer = input('答错了，神龙表示不想理你……好吧，再给你一次机会：')

print ('你已经成功召唤神龙！')