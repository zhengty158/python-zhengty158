# -*- coding: utf-8 -*-
# 工伤待遇计算器
# 该代码适合律师、法务、人力资源管理人员使用
# 该代码中某些基数使用广州市相关标准（比如上年度职工平均工资），而且是2016年度的，各位使用时请根据所在地区及当年最新相关标准修改
# 已增加重复计算功能
# 已增加输入提示符

print('\n\n        工伤待遇计算器\n\n')

Deng_Ji = int(input("请输入伤残等级（数字）：\n>  "))

print('是否解除劳动合同？')
SiFou_JieChu = int(input('解除请按1，不解除请按2：\n>  '))

# 以下函数为程序核心代码
def Jishuan_Gongshi(Deng_Ji, SiFou_JieChu):
    # 获取工伤情况的基本资料：
    GongZhi_1 = float(input("请输入受伤前12个月平均工资（数字）：\n>  "))
    YuePing_GongZhi = int('6764')   # 广州市2016年公布的上年度职工月平均工资
    HuoShiBuZhu_JiaGe = int('35')   # 住院伙食补助标准
    ZhuYuan_TianShu = float(input('请输入住院天数（数字）：\n>  '))
    HuLi_TianShu = int(input('请输入住院护理天数（非生活护理）：\n>  '))
    TingGongLiuXinQi_YueShu = float(input('请输入停工留薪期月数（数字）：\n>  '))
    TingGongLiuXinQi_TianShu = int(input('请输入停工留薪期间，\n除完整月份之外的工作日天数（数字）：\n>  '))
    TingGongLiuXinQi_ShiFaGongZhi = float(input('请输入停工留薪期实发工资总额（数字）：\n>  '))
    # 告知用户，并限定工资计算基数在合法范围内：
    if SiFou_JieChu == 1:
        GongZhi_2 = float(input("\n请输入解除劳动合同前12个月平均工资\n（本计算器将自动比较受伤前工资，\n自动选择较高者作为“一次性工伤医疗补助金”“一次性伤残就业补助金”的计算基数）：\n>  "))
        print('\n请注意计算基数的法定范围：\n2016年7月公布的广州职工平均工资6764元')
        print('计算基数必须大于等于4058.4元=6764元×60%')
        print('计算基数必须小于等于20292元=6764元×300%')
        print('即：4058.4元<=计算基数<=20292元')
        
        if GongZhi_1 < YuePing_GongZhi * 0.6:
            GongZhi_1 = YuePing_GongZhi * 0.6
            print('\n受伤前12个月平均工资低于广州职工平均工资6764元的60%，\n本计算器将采用4058.4元作为计算基数！\n')
        elif GongZhi_1 > YuePing_GongZhi * 3:
                GongZhi_1 = YuePing_GongZhi * 3
                print('\n受伤前12个月平均工资高于广州职工平均工资6764元的300%，\n本计算器将采用20292元作为计算基数！\n')
                
    if SiFou_JieChu == 1:
        if GongZhi_2 < YuePing_GongZhi * 0.6:
            GongZhi_2 = YuePing_GongZhi * 0.6
            print('\n解除劳动合同前12个月平均工资低于广州职工平均工资6764元的60%，\n本计算器将采用4058.4元作为计算基数！\n')
        elif GongZhi_2 > YuePing_GongZhi * 3:
            GongZhi_2 = YuePing_GongZhi * 3
            print('\n解除劳动合同前12个月平均工资高于广州职工平均工资6764元的300%，\n本计算器将采用20292元作为计算基数！\n')
    # 根据用户输入的伤残等级、是否解除劳动合同，调用相应等级的费率及情况计算工伤待遇：  
    Deng_Ji -= 1
    Fei_Lv = [[0.6,27,0.9],[0.5,25,0.85],[0.4,23,0.8],[0.3,21,0.75],[18,10,50,0.7],[16,8,40,0.6],[13,6,25],[11,4,15],[9,2,8],[7,1,4]]
    Fei_Lv1 = Fei_Lv[Deng_Ji][0]
    Fei_Lv2 = Fei_Lv[Deng_Ji][1]
    Fei_Lv3 = Fei_Lv[Deng_Ji][2]
    if Deng_Ji == 4 or Deng_Ji == 5:
        Fei_Lv4 = Fei_Lv[Deng_Ji][3]
    if (Deng_Ji+1) > 4:
        print('\n\n根据以上条件计算，工伤待遇为：\n')
        a = float('%.2f' % (GongZhi_1 * Fei_Lv1))
        print('一次性伤残补助金：', a, '元\n')
        if SiFou_JieChu == 1:
            b = float('%.2f' % (max(GongZhi_1, GongZhi_2) * Fei_Lv2))
            c = float('%.2f' % (max(GongZhi_1, GongZhi_2) * Fei_Lv3))
            print('一次性工伤医疗补助金：', b, '元\n')
            print('一次性伤残就业补助金：', c, '元\n')   
        if (SiFou_JieChu == 2) and (DengJi == 4 or DengJi == 5):
                print('伤残津贴（每月）：',float('%.2f' % (GongZhi_1 * Fei_Lv4)),'元\n')
    elif (Deng_Ji+1) <= 4:
        ZiLi_ZhangAi = int(input('请输入生活自理障碍程度等级（数字）：>  '))
        ZiLi_ZhangAi -= 1
        ShengHuoHuLiFei_DengJi_FeiLv = [0.6, 0.5, 0.4, 0.3]
        temp1 = float('%.2f' % (YuePing_GongZhi * ShengHuoHuLiFei_DengJi_FeiLv[ZiLi_ZhangAi]))
        print('\n\n根据以上条件计算，工伤待遇为：\n')
        print('生活护理费（每月）:', temp1, '元', '（生活护理费以上年广州职工平均工资为计算基数）\n')
        print('一次性伤残补助金：',float('%.2f' % (GongZhi_1 * Fei_Lv2)),'元\n')
        print('伤残津贴（每月直至退休）：',float('%.2f' % (GongZhi_1 * Fei_Lv3)),'元\n')
    d = HuLi_TianShu * 80
    print('住院护理费：', d, '元', '（广州一般护理费标准认定为80元/日）\n')
    e = float('%.2f' % (ZhuYuan_TianShu * HuoShiBuZhu_JiaGe))
    print('住院伙食补助：', e, '元\n')
    f = float('%.2f' % ((TingGongLiuXinQi_YueShu * GongZhi_1) + TingGongLiuXinQi_TianShu * (GongZhi_1 / 21.75)))
    print('停工留薪期待遇（应发）：', f, '元\n')
    g = float('%.2f' % ((TingGongLiuXinQi_YueShu * GongZhi_1) + TingGongLiuXinQi_TianShu * (GongZhi_1 / 21.75) - TingGongLiuXinQi_ShiFaGongZhi ))
    print('停工留薪期待遇（补差额）：', g, '元\n')
    if ((Deng_Ji+1) > 4) and (SiFou_JieChu == 1):
        print('\n以上待遇应发总额为：', float('%.2f' % (a + b + c + d + e + f)), '元')
        print('\n以上待遇补差总额为：', float('%.2f' % (a + b + c + d + e + g)), '元')
    elif ((Deng_Ji+1) > 4) and (SiFou_JieChu == 2):
        print('\n以上待遇应发总额为：', float('%.2f' % (a + d + e + f)), '元')
        print('\n以上待遇补差总额为：', float('%.2f' % (a + d + e + g)), '元')
    elif (Deng_Ji == 4 or Deng_Ji == 5) and (SiFou_JieChu == 1):
        print('\n以上待遇应发总额为（不含伤残津贴）：', float('%.2f' % (a + b + c + d + e + f)), '元')
        print('\n以上待遇补差总额为（不含伤残津贴）：', float('%.2f' % (a + b + c + d + e + g)), '元')
    elif (Deng_Ji == 4 or Deng_Ji == 5) and (SiFou_JieChu == 2):
        print('\n以上待遇应发总额为（不含伤残津贴）：', float('%.2f' % (a + d + e + f)), '元')
        print('\n以上待遇补差总额为（不含伤残津贴）：', float('%.2f' % (a + d + e + g)), '元')

    
Jishuan_Gongshi(Deng_Ji, SiFou_JieChu)

# 可重复计算功能
print('\n\n是否计算下一个？是=1，否=2')
SiFou_JiXu = input('>  ')

while SiFou_JiXu == '1':
    print('\n\n        工伤待遇计算器\n\n')
    Deng_Ji = int(input("请输入伤残等级（数字）：\n>  "))
    print('是否解除劳动合同？')
    SiFou_JieChu = int(input('解除请按1，不解除请按2：\n>  '))
    Jishuan_Gongshi(Deng_Ji, SiFou_JieChu)
    print('是否计算下一个？是=1，否=2')
    SiFou_JiXu = input('>  ')

input('\n\n\n\n按回车键退出')
