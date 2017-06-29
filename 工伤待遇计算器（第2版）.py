# 工伤待遇计算器
# 该程序适合律师、法务、人力资源管理人员使用
# 该程序中某些基数使用广州市相关标准（比如上年度职工平均工资），而且是2016年度的，各位使用时请根据所在地区及当年最新相关标准修改
# 增加“生活自理障碍程度等级：0级”，方便计算有“生活自理障碍程度等级：未达级”的1~4级伤残人员待遇

# -*- coding: utf-8 -*-

import math

while True:
    
    print('\n\n        工伤待遇计算器\n\n')
    Deng_Ji = int(input("请输入伤残等级（数字）：\n>  "))
    print('是否解除劳动合同？')
    SiFou_JieChu = int(input('解除请按1，不解除请按2：\n>  '))
    
    # 以下函数为程序核心程序
    def Jishuan_Gongshi(Deng_Ji, SiFou_JieChu):
        # 获取工伤情况的基本资料：
        GongZhi_1 = float(input("请输入受伤前12个月平均工资（数字）：\n>  "))
        GongZhi_TingGongLiuXin = GongZhi_1   # 要按工伤前12个月平均实发工资，计算停工留薪期应发工资，并不是按社会职工平均工资的60%-300%
        YuePing_GongZhi = int('6764')   # 广州市2016年公布的上年度职工月平均工资
        HuoShiBuZhu_JiaGe = int('35')   # 住院伙食补助标准
        ZhuYuan_TianShu = float(input('请输入住院天数（数字）：\n>  '))
        HuLi_TianShu = int(input('请输入住院护理天数（非生活护理）：\n>  '))
        TingGongLiuXinQi_YueShu = float(input('请输入停工留薪期月数（数字）：\n>  '))
        TingGongLiuXinQi_TianShu = int(input('请输入停工留薪期间，\n除完整月份之外的工作日天数（数字）：\n>  '))
        TingGongLiuXinQi_ShiFaGongZhi = float(input('请输入停工留薪期实发工资总额（数字）：\n>  '))
        # 告知用户，并限定工资计算基数在法定范围内：
        if SiFou_JieChu == 1:
            GongZhi_2 = float(input("\n请输入解除劳动合同前12个月平均工资\n（本计算器将自动比较受伤前工资，\n自动选择较高者作为“一次性工伤医疗补助金”“一次性伤残就业补助金”的计算基数）：\n>  "))
            if GongZhi_2 < YuePing_GongZhi * 0.6:
                GongZhi_2 = YuePing_GongZhi * 0.6
                print('\n解除劳动合同前12个月平均工资低于广州职工平均工资6764元的60%，即4058.4元！\n')
            elif GongZhi_2 > YuePing_GongZhi * 3:
                GongZhi_2 = YuePing_GongZhi * 3
                print('\n解除劳动合同前12个月平均工资高于广州职工平均工资6764元的300%，即20292元！\n')
            print('根据你输入的受伤前和解除劳动合同前12个月平均工资，和广州职工平均工资，\n本计算器将采用{GongZhi}元作为“一次性工伤医疗补助金”+“一次性伤残就业补助金”的计算基数'.format(GongZhi = max(GongZhi_1, GongZhi_2)))
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
        # 根据用户输入的伤残等级、是否解除劳动合同，调用相应等级的费率及情况计算工伤待遇：
        FeiLv_Biao = {'dengji1':(0.6,27,0.9), 'dengji2':(0.5,25,0.85), 'dengji3':(0.4,23,0.8), 'dengji4':(0.3,21,0.75), 'dengji5':(18,10,50,0.7),
                      'dengji6':(16,8,40,0.6), 'dengji7':(13,6,25), 'dengji8':(11,4,15), 'dengji9':(9,2,8), 'dengji10':(7,1,4)}
        Fei_Lv1 = FeiLv_Biao['dengji%d' % Deng_Ji][0]  # 根据等级提取费率
        Fei_Lv2 = FeiLv_Biao['dengji%d' % Deng_Ji][1]
        Fei_Lv3 = FeiLv_Biao['dengji%d' % Deng_Ji][2]
        if Deng_Ji == 5 or Deng_Ji == 6:
            Fei_Lv4 = Fei_Lv['dengji%d' % Deng_Ji][3]
        if Deng_Ji > 4:
            print('\n\n根据以上条件计算，工伤待遇为：\n')
            temp_a = GongZhi_1 * Fei_Lv1
            print('一次性伤残补助金：', temp_a, '元\n')
            if SiFou_JieChu == 1:
                temp_b = max(GongZhi_1, GongZhi_2) * Fei_Lv2
                temp_c = max(GongZhi_1, GongZhi_2) * Fei_Lv3
                print('一次性工伤医疗补助金：', temp_b, '元\n')
                print('一次性伤残就业补助金：', temp_c, '元\n')
            if (SiFou_JieChu == 2) and (Deng_Ji == 5 or Deng_Ji == 6):
                print('伤残津贴（每月）：',float('%.2f' % (GongZhi_1 * Fei_Lv4)),'元\n')
        elif Deng_Ji <= 4:
            ZiLi_ZhangAi = int(input('请输入生活自理障碍程度等级（数字）：>  '))
            ShengHuoHuLiFei_DengJi_FeiLv = {'dengji0':0, 'dengji1':0.6, 'dengji2':0.5, 'dengji3':0.4, 'dengji4':0.3}    # 字典中增加了'dengji0':0
            temp1 = float('%.2f' % (YuePing_GongZhi * ShengHuoHuLiFei_DengJi_FeiLv['dengji%d' % ZiLi_ZhangAi]))
            print('\n\n根据以上条件计算，工伤待遇为：\n')
            print('生活护理费（每月）:', temp1, '元', '（生活护理费以上年广州职工平均工资为计算基数）\n')
            print('一次性伤残补助金：',float('%.2f' % (GongZhi_1 * Fei_Lv2)),'元\n')
            print('伤残津贴（每月直至退休）：',float('%.2f' % (GongZhi_1 * Fei_Lv3)),'元\n')
        temp_d = HuLi_TianShu * 80
        print('住院护理费：', temp_d, '元', '（广州一般护理费标准认定为80元/日）\n')
        temp_e = ZhuYuan_TianShu * HuoShiBuZhu_JiaGe
        print('住院伙食补助：', temp_e, '元\n')
        temp_f = (TingGongLiuXinQi_YueShu * GongZhi_TingGongLiuXin) + TingGongLiuXinQi_TianShu * GongZhi_TingGongLiuXin / 21.75)
        print('停工留薪期待遇（应发）：', temp_f, '元\n')
        temp_g = (TingGongLiuXinQi_YueShu * GongZhi_TingGongLiuXin) + TingGongLiuXinQi_TianShu * (GongZhi_TingGongLiuXin / 21.75) - TingGongLiuXinQi_ShiFaGongZhi
        print('停工留薪期待遇（补差额）：', temp_g, '元\n')
        if (Deng_Ji > 4) and (SiFou_JieChu == 1):
            print('\n以上待遇应发总额为：', math.fsum([temp_a, temp_b, temp_c, temp_d, temp_e, temp_f]), '元')
            print('\n以上待遇补差总额为：', math.fsum([temp_a, temp_b, temp_c, temp_d, temp_e, temp_g]), '元')
        elif (Deng_Ji > 4) and (SiFou_JieChu == 2):
            print('\n以上待遇应发总额为：', math.fsum([temp_a, temp_d, temp_e, temp_f]), '元')
            print('\n以上待遇补差总额为：', math.fsum([temp_a, temp_d, temp_e, temp_g]), '元')
        elif (Deng_Ji == 5 or Deng_Ji == 6) and (SiFou_JieChu == 1):
            print('\n以上待遇应发总额为（不含伤残津贴）：', math.fsum([temp_a, temp_b, temp_c, temp_d, temp_e, temp_f]), '元')
            print('\n以上待遇补差总额为（不含伤残津贴）：', math.fsum([temp_a, temp_b, temp_c, temp_d, temp_e, temp_g]), '元')
        elif (Deng_Ji == 5 or Deng_Ji == 6) and (SiFou_JieChu == 2):
            print('\n以上待遇应发总额为（不含伤残津贴）：', math.fsum([temp_a, temp_d, temp_e, temp_f]), '元')
            print('\n以上待遇补差总额为（不含伤残津贴）：', math.fsum([temp_a, temp_d, temp_e, temp_g]), '元')
    

    Jishuan_Gongshi(Deng_Ji, SiFou_JieChu)
