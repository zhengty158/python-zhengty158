# -*- coding: utf-8 -*-
# 已增加计算停工留薪期工资的功能：让人输入工作日天数、停工留薪期实发工资，由电脑计算应发工资、补差额
# 还需增加输出为txt文档的功能

print('工伤待遇计算器\n')
gongzhi1 = float(input("请输入受伤前12个月平均工资（数字）："))
dengji = input("请输入伤残等级（数字）：")
yuepinggongzhi = int('6764')
huoshibuzhu = float(input('请输入住院天数（数字）：'))
tinggongliuxinqiyueshu = int(input('请输入停工留薪期月数（数字）：'))
tinggongliuxinqitianshu = int(input('请输入停工留薪期间，除完整月份之外的工作日天数（数字）：'))
tinggongliuxinqishifagongzhi = float(input('请输入停工留薪期实发工资总额（数字）：'))

if dengji == '10':
		print("是否解除劳动合同？")
		temp = input('\n解除请按1，保留请按2：\n')
		if temp == '1':
			gongzhi2 = float(input("请输入解除劳动合同前12个月平均工资（数字）："))
			if gongzhi2 <= gongzhi1:
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 7)),'元')
				print('一次性工伤医疗补助金：',float('%.2f' % (gongzhi1 * 1)),'元')
				print('一次性伤残就业补助金：',float('%.2f' % (float('%.2f' % (gongzhi1 * 4)))),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
			if gongzhi2 > gongzhi1:
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 7)),'元')
				print('一次性工伤医疗补助金：',float('%.2f' % (gongzhi2 * 1)),'元')
				print('一次性伤残就业补助金：',float('%.2f' % (float('%.2f' % (gongzhi2 * 4)))),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
		if temp == '2':
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 7)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
			
if dengji == '9':
		print("是否解除劳动合同？")
		temp = input('\n解除请按1，保留请按2：\n')
		if temp == '1':
			gongzhi2 = float(input("请输入解除劳动合同前12个月平均工资（数字）："))
			if gongzhi2 <= gongzhi1:
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 9)),'元')
				print('一次性工伤医疗补助金：',float('%.2f' % (gongzhi1 * 2)),'元')
				print('一次性伤残就业补助金：',float('%.2f' % (gongzhi1 * 8)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
			if gongzhi2 > gongzhi1:
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 9)),'元')
				print('一次性工伤医疗补助金：',float('%.2f' % (gongzhi2 * 9)),'元')
				print('一次性伤残就业补助金：',float('%.2f' % (gongzhi2 * 9)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
		if temp == '2':
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',gongzhi1 * 9,'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
				
if dengji == '8':
		print("是否解除劳动合同？")
		temp = input('\n解除请按1，保留请按2：\n')
		if temp == '1':
			gongzhi2 = float(input("请输入解除劳动合同前12个月平均工资（数字）："))
			if gongzhi2 <= gongzhi1:
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 11)),'元')
				print('一次性工伤医疗补助金：',float('%.2f' % (gongzhi1 * 4)),'元')
				print('一次性伤残就业补助金：',float('%.2f' % (gongzhi1 * 15)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
			if gongzhi2 > gongzhi1:
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 11)),'元')
				print('一次性工伤医疗补助金：',float('%.2f' % (gongzhi2 * 4)),'元')
				print('一次性伤残就业补助金：',float('%.2f' % (gongzhi2 * 15)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
		if temp == '2':
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 11)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
				
if dengji == '7':
		print("是否解除劳动合同？")
		temp = input('\n解除请按1，保留请按2：\n')
		if temp == '1':
			gongzhi2 = float(input("请输入解除劳动合同前12个月平均工资（数字）："))
			if gongzhi2 <= gongzhi1:
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 13)),'元')
				print('一次性工伤医疗补助金：',float('%.2f' % (gongzhi1 * 6)),'元')
				print('一次性伤残就业补助金：',float('%.2f' % (gongzhi1 * 25)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
			if gongzhi2 > gongzhi1:
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 13)),'元')
				print('一次性工伤医疗补助金：',float('%.2f' % (gongzhi2 * 6)),'元')
				print('一次性伤残就业补助金：',float('%.2f' % (gongzhi2 * 25)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
		if temp == '2':
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 13)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
				
if dengji == '6':
		print("是否解除劳动合同？")
		temp = input('\n解除请按1，保留请按2：\n')
		if temp == '1':
			gongzhi2 = float(input("请输入解除劳动合同前12个月平均工资（数字）："))
			if gongzhi2 <= gongzhi1:
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 16)),'元')
				print('一次性工伤医疗补助金：',float('%.2f' % (gongzhi1 * 8)),'元')
				print('一次性伤残就业补助金：',float('%.2f' % (gongzhi1 * 40)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
			if gongzhi2 > gongzhi1:
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 16)),'元')
				print('一次性工伤医疗补助金：',float('%.2f' % (gongzhi2 * 8)),'元')
				print('一次性伤残就业补助金：',float('%.2f' % (gongzhi2 * 40)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
		if temp == '2':
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 16)),'元')
				print('伤残津贴（每月）：',float('%.2f' % (gongzhi1 * 0.6)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
				
if dengji == '5':
		print("是否解除劳动合同？")
		temp = input('\n解除请按1，保留请按2：\n')
		if temp == '1':
			gongzhi2 = float(input("请输入解除劳动合同前12个月平均工资（数字）："))
			if gongzhi2 <= gongzhi1:
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 18)),'元')
				print('一次性工伤医疗补助金：',float('%.2f' % (gongzhi1 * 10)),'元')
				print('一次性伤残就业补助金：',float('%.2f' % (gongzhi1 * 50)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
			if gongzhi2 > gongzhi1:
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 18)),'元')
				print('一次性工伤医疗补助金：',float('%.2f' % (gongzhi2 * 10)),'元')
				print('一次性伤残就业补助金：',float('%.2f' % (gongzhi2 * 50)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
		if temp == '2':
				print('\n\n根据以上条件计算，工伤待遇为：\n')
				print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 18)),'元')
				print('伤残津贴（每月）：',float('%.2f' % (gongzhi1 * 0.7)),'元')
				print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
				print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
				print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
				
if dengji == '4':
		temp1 = yuepinggongzhi * 0.3
		temp2 = float('%.2f' % temp1)
		print('\n\n根据以上条件计算，工伤待遇为：\n')
		print('生活护理费（每月）:',temp2,'元','（2016年7月公布的职工平均工资是6764元）')
		print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 21)),'元')
		print('伤残津贴（每月直至退休）：',float('%.2f' % (gongzhi1 * 0.75)),'元')
		print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
		print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
		print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
		
if dengji == '3':
		temp1 = yuepinggongzhi * 0.4
		temp2 = float('%.2f' % temp1)
		print('\n\n根据以上条件计算，工伤待遇为：\n')
		print('生活护理费（每月）:',temp2,'元','（2016年7月公布的职工平均工资是6764元）')
		print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 23)),'元')
		print('伤残津贴（每月直至退休）：',float('%.2f' % (gongzhi1 * 0.8)),'元')
		print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
		print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
		print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
		
if dengji == '2':
		temp1 = yuepinggongzhi * 0.5
		temp2 = float('%.2f' % temp1)
		print('\n\n根据以上条件计算，工伤待遇为：\n')
		print('生活护理费（每月）:',temp2,'元','（2016年7月公布的职工平均工资是6764元）')
		print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 25)),'元')
		print('伤残津贴（每月直至退休）：',float('%.2f' % (gongzhi1 * 0.85)),'元')
		print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
		print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
		print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')
		
if dengji == '1':
		temp1 = yuepinggongzhi * 0.6
		temp2 = float('%.2f' % temp1)
		print('\n\n根据以上条件计算，工伤待遇为：\n')
		print('生活护理费（每月）:',temp2,'元','（2016年7月公布的职工平均工资是6764元）')
		print('一次性伤残补助金：',float('%.2f' % (gongzhi1 * 27)),'元')
		print('伤残津贴（每月直至退休）：',float('%.2f' % (gongzhi1 * 0.9)),'元')
		print('住院伙食补助：',float('%.2f' % (huoshibuzhu * 35)),'元')
		print('停工留薪期待遇（应发）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75))),'元')
		print('停工留薪期待遇（补差额）：',float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi )),'元')

input('\n\n按回车键退出')
