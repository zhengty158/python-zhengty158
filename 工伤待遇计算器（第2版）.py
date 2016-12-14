# -*- coding: utf-8 -*-
# 工伤待遇计算器
# 已增加计算停工留薪期工资的功能：让用户输入工作日天数、停工留薪期实发工资，由电脑计算应发工资、补差额
# 已增加限定工资计算基数范围的功能：限定工资基数在“社会职工平均工资*60%——社会职工平均工资*300%”之内，并增加字幕提示
# 已优化排版显示效果、并大幅减少重复代码，函数精简到只有一个
# 已增加统计工伤待遇总额的功能
# 还需增加：输出计算结果为txt文档的功能、计算解除劳动合同经济补偿金的功能

print('\n\n        工伤待遇计算器\n\n')
gongzhi1 = float(input("请输入受伤前12个月平均工资（数字）：\n"))
dengji = int(input("请输入伤残等级（数字）：\n"))
yuepinggongzhi = int('6764')
huoshibuzhujiage = int('35')
zhuyuantianshu = float(input('请输入住院天数（数字）：\n'))
hulitianshu = int(input('请输入护理天数（数字）：\n'))
tinggongliuxinqiyueshu = float(input('\n请输入停工留薪期月数（数字）：\n'))
tinggongliuxinqitianshu = int(input('请输入停工留薪期间，\n除完整月份之外的工作日天数（数字）：\n'))
tinggongliuxinqishifagongzhi = float(input('请输入停工留薪期实发工资总额（数字）：\n'))
print('\n是否解除劳动合同？')
jiechuhetong = int(input('解除请按1，不解除请按2：\n'))
if jiechuhetong == 1:
    gongzhi2 = float(input("\n请输入解除劳动合同前12个月平均工资\n（本计算器将自动比较受伤前工资，\n自动选择较高者作为“一次性工伤医疗补助金”“一次性伤残就业补助金”的计算基数）："))
print('\n请注意计算基数的法定范围：\n2016年7月公布的广州职工平均工资6764元')
print('计算基数必须大于等于4058.4元=6764元×60%')
print('计算基数必须小于等于20292元=6764元×300%')
print('即：4058.4元<=计算基数<=20292元')

if gongzhi1 < yuepinggongzhi * 0.6:
    gongzhi1 = yuepinggongzhi * 0.6
    print('\n受伤前12个月平均工资低于广州职工平均工资6764元的60%，\n本计算器将采用4058.4元作为计算基数！\n')

elif gongzhi1 > yuepinggongzhi * 3:
    gongzhi1 = yuepinggongzhi * 3
    print('\n受伤前12个月平均工资高于广州职工平均工资6764元的300%，\n本计算器将采用20292元作为计算基数！\n')

if jiechuhetong == 1:
    if gongzhi2 < yuepinggongzhi * 0.6:
        gongzhi2 = yuepinggongzhi * 0.6
        print('\n解除劳动合同前12个月平均工资低于广州职工平均工资6764元的60%，\n本计算器将采用4058.4元作为计算基数！\n')
    elif gongzhi2 > yuepinggongzhi * 3:
        gongzhi2 = yuepinggongzhi * 3
        print('\n解除劳动合同前12个月平均工资高于广州职工平均工资6764元的300%，\n本计算器将采用20292元作为计算基数！\n')

def jishuangongshi(x,y):
    x = x - 1
    feilv = [[0.6,27,0.9],[0.5,25,0.85],[0.4,23,0.8],[0.3,21,0.75],[18,10,50,0.7],[16,8,40,0.6],[13,6,25],[11,4,15],[9,2,8],[7,1,4]]
    feilv1 = feilv[x][0]
    feilv2 = feilv[x][1]
    feilv3 = feilv[x][2]
    if x == 4 or x == 5:
        feilv4 = feilv[x][3]
    temp1 = yuepinggongzhi * feilv1
    temp2 = float('%.2f' % temp1)
    if (x+1) > 4:
        print('\n\n根据以上条件计算，工伤待遇为：\n')
        a = float('%.2f' % (gongzhi1 * feilv1))
        print('一次性伤残补助金：', a, '元\n')
        if y == 1:
            b = float('%.2f' % (max(gongzhi1, gongzhi2) * feilv2))
            c = float('%.2f' % (max(gongzhi1, gongzhi2) * feilv3))
            print('一次性工伤医疗补助金：', b, '元\n')
            print('一次性伤残就业补助金：', c, '元\n')   
        if y == 2:
            if x == 4 or x == 5:
                print('伤残津贴（每月）：',float('%.2f' % (gongzhi1 * feilv4)),'元\n')
    elif (x+1) <= 4:
        print('\n\n根据以上条件计算，工伤待遇为：\n')
        print('生活护理费（每月）:\n',temp2,'元\n')
        print('一次性伤残补助金：\n',float('%.2f' % (gongzhi1 * feilv2)),'元\n')
        print('伤残津贴（每月直至退休）：\n',float('%.2f' % (gongzhi1 * feilv3)),'元\n')
    d = hulitianshu * 80
    print('护理费：', d, '元', '（广州一般护理费标准认定为80元/日）\n')
    e = float('%.2f' % (zhuyuantianshu * huoshibuzhujiage))
    print('住院伙食补助：', e, '元\n')
    f = float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75)))
    print('停工留薪期待遇（应发）：', f, '元\n')
    g = float('%.2f' % ((tinggongliuxinqiyueshu * gongzhi1) + tinggongliuxinqitianshu * (gongzhi1 / 21.75) - tinggongliuxinqishifagongzhi ))
    print('停工留薪期待遇（补差额）：', g, '元\n')
    if (x+1) > 4:
        print('\n以上待遇应发总额为：', (a + b + c + d + e + f), '元')
        print('\n以上待遇补差总额为：', (a + b + c + d + e + g), '元')
    if x == 4 or x == 5:
        print('\n以上待遇应发总额为（不含伤残津贴）：', (a + b + c + d + e + f), '元')
        print('\n以上待遇补差总额为（不含伤残津贴）：', (a + b + c + d + e + g), '元')
    
jishuangongshi(dengji,jiechuhetong)

input('\n\n\n\n按回车键退出')
