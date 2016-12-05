# -*- coding: utf-8 -*-
# 为了减少简单重复劳动，我写了这堆代码
# 功能是计算1-10级的工伤待遇

print('工伤待遇计算器\n')
gongzhi1 = float(input("请输入受伤前12个月平均工资（数字）："))
dengji = input("请输入伤残等级（数字）：")
yuepinggongzhi = int('6764')

if dengji == '10':
		print("是否解除劳动合同？")
		temp = input('\n解除请按1，保留请按2：\n')
		if temp == '1':
			gongzhi2 = float(input("请输入解除劳动合同前12个月平均工资（数字）："))
			if gongzhi2 <= gongzhi1:
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 7,'元')
				print('一次性工伤医疗补助金',gongzhi1 * 1,'元')
				print('一次性伤残就业补助金',gongzhi1 * 4,'元')
			if gongzhi2 > gongzhi1:
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 7,'元')
				print('一次性工伤医疗补助金',gongzhi2 * 1,'元')
				print('一次性伤残就业补助金',gongzhi2 * 4,'元')
		if temp == '2':
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 7,'元')
			
if dengji == '9':
		print("是否解除劳动合同？")
		temp = input('\n解除请按1，保留请按2：\n')
		if temp == '1':
			gongzhi2 = float(input("请输入解除劳动合同前12个月平均工资（数字）："))
			if gongzhi2 <= gongzhi1:
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 9,'元')
				print('一次性工伤医疗补助金',gongzhi1 * 2,'元')
				print('一次性伤残就业补助金',gongzhi1 * 8,'元')
			if gongzhi2 > gongzhi1:
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 9,'元')
				print('一次性工伤医疗补助金',gongzhi2 * 2,'元')
				print('一次性伤残就业补助金',gongzhi2 * 8,'元')
		if temp == '2':
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 9,'元')
				
if dengji == '8':
		print("是否解除劳动合同？")
		temp = input('\n解除请按1，保留请按2：\n')
		if temp == '1':
			gongzhi2 = float(input("请输入解除劳动合同前12个月平均工资（数字）："))
			if gongzhi2 <= gongzhi1:
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 11,'元')
				print('一次性工伤医疗补助金',gongzhi1 * 4,'元')
				print('一次性伤残就业补助金',gongzhi1 * 15,'元')
			if gongzhi2 > gongzhi1:
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 11,'元')
				print('一次性工伤医疗补助金',gongzhi2 * 4,'元')
				print('一次性伤残就业补助金',gongzhi2 * 15,'元')
		if temp == '2':
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 11,'元')
				
if dengji == '7':
		print("是否解除劳动合同？")
		temp = input('\n解除请按1，保留请按2：\n')
		if temp == '1':
			gongzhi2 = float(input("请输入解除劳动合同前12个月平均工资（数字）："))
			if gongzhi2 <= gongzhi1:
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 13,'元')
				print('一次性工伤医疗补助金',gongzhi1 * 6,'元')
				print('一次性伤残就业补助金',gongzhi1 * 25,'元')
			if gongzhi2 > gongzhi1:
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 13,'元')
				print('一次性工伤医疗补助金',gongzhi2 * 6,'元')
				print('一次性伤残就业补助金',gongzhi2 * 25,'元')
		if temp == '2':
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 13,'元')
				
if dengji == '6':
		print("是否解除劳动合同？")
		temp = input('\n解除请按1，保留请按2：\n')
		if temp == '1':
			gongzhi2 = float(input("请输入解除劳动合同前12个月平均工资（数字）："))
			if gongzhi2 <= gongzhi1:
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 16,'元')
				print('一次性工伤医疗补助金',gongzhi1 * 8,'元')
				print('一次性伤残就业补助金',gongzhi1 * 40,'元')
			if gongzhi2 > gongzhi1:
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 16,'元')
				print('一次性工伤医疗补助金',gongzhi2 * 8,'元')
				print('一次性伤残就业补助金',gongzhi2 * 40,'元')
		if temp == '2':
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 16,'元')
				print('伤残津贴（每月）',gongzhi1 * 0.6,'元')
				
if dengji == '5':
		print("是否解除劳动合同？")
		temp = input('\n解除请按1，保留请按2：\n')
		if temp == '1':
			gongzhi2 = float(input("请输入解除劳动合同前12个月平均工资（数字）："))
			if gongzhi2 <= gongzhi1:
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 18,'元')
				print('一次性工伤医疗补助金',gongzhi1 * 10,'元')
				print('一次性伤残就业补助金',gongzhi1 * 50,'元')
			if gongzhi2 > gongzhi1:
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 18,'元')
				print('一次性工伤医疗补助金',gongzhi2 * 10,'元')
				print('一次性伤残就业补助金',gongzhi2 * 50,'元')
		if temp == '2':
				print('\n工伤待遇为：\n')
				print('一次性伤残补助金:',gongzhi1 * 18,'元')
				print('伤残津贴（每月）',gongzhi1 * 0.7,'元')
				
if dengji == '4':
		temp1 = yuepinggongzhi * 0.3
		temp2 = float('%.2f' % temp1)
		print('\n工伤待遇为：\n')
		print('生活护理费（每月）:',temp2,'元','（2016年7月公布的职工平均工资是6764元）')
		print('一次性伤残补助金:',gongzhi1 * 21,'元')
		print('伤残津贴（每月直至退休）',gongzhi1 * 0.75,'元')
		
if dengji == '3':
		temp1 = yuepinggongzhi * 0.4
		temp2 = float('%.2f' % temp1)
		print('\n工伤待遇为：\n')
		print('生活护理费（每月）:',temp2,'元','（2016年7月公布的职工平均工资是6764元）')
		print('一次性伤残补助金:',gongzhi1 * 23,'元')
		print('伤残津贴（每月直至退休）',gongzhi1 * 0.8,'元')
		
if dengji == '2':
		temp1 = yuepinggongzhi * 0.5
		temp2 = float('%.2f' % temp1)
		print('\n工伤待遇为：\n')
		print('生活护理费（每月）:',temp2,'元','（2016年7月公布的职工平均工资是6764元）')
		print('一次性伤残补助金:',gongzhi1 * 25,'元')
		print('伤残津贴（每月直至退休）',gongzhi1 * 0.85,'元')
		
if dengji == '1':
		temp1 = yuepinggongzhi * 0.6
		temp2 = float('%.2f' % temp1)
		print('\n工伤待遇为：\n')
		print('生活护理费（每月）:',temp2,'元','（2016年7月公布的职工平均工资是6764元）')
		print('一次性伤残补助金:',gongzhi1 * 27,'元')
		print('伤残津贴（每月直至退休）',gongzhi1 * 0.9,'元')
