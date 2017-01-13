# -*- coding: utf-8 -*-
# 工伤待遇计算器
# 已将所有代码尽量精简为一个函数，尽量实现代码模块化
# 已改写变量名，增强代码可读性
# 该代码适合律师、法务、人力资源管理人员使用
# 该代码中某些基数使用广州市相关标准（比如上年度职工平均工资），而且是2016年度的，各位使用时请根据所在地区及当年最新相关标准修改
# 还需增加：输出计算结果为txt文档的功能

# 这一版删除了按提示输入工伤情况数据的代码，将其改为由参数获取，然后直接得到计算结果
# DengJi = 工伤等级   SiFou_JieChu = 是否解除合同（1=是，2=否）  GongZhi_1 = 受伤前12个月平均工资  GongZhi_2 = 解除劳动合同前12个月平均工资

def jsq(DengJi, SiFou_JieChu, GongZhi_1, ZhuYuan_TianShu, HuLi_TianShu, TingGongLiuXinQi_YueShu,
        TingGongLiuXinQi_TianShu, TingGongLiuXinQi_ShiFaGongZhi, GongZhi_2):
    YuePing_GongZhi = int('6764')
    HuoShiBuZhu_JiaGe = int('35')
    # 告知用户，并限定工资计算基数在合法范围内：
    if SiFou_JieChu == 1:
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
    DengJi -= 1
    Fei_Lv = [[0.6,27,0.9],[0.5,25,0.85],[0.4,23,0.8],[0.3,21,0.75],[18,10,50,0.7],[16,8,40,0.6],[13,6,25],[11,4,15],[9,2,8],[7,1,4]]
    Fei_Lv1 = Fei_Lv[DengJi][0]
    Fei_Lv2 = Fei_Lv[DengJi][1]
    Fei_Lv3 = Fei_Lv[DengJi][2]
    if DengJi == 4 or DengJi == 5:
        Fei_Lv4 = Fei_Lv[DengJi][3]
    if (DengJi+1) > 4:
        print('\n\n根据以上条件计算，工伤待遇为：\n')
        a = float('%.2f' % (GongZhi_1 * Fei_Lv1))
        print('一次性伤残补助金：', a, '元\n')
        if SiFou_JieChu == 1:
            b = float('%.2f' % (max(GongZhi_1, GongZhi_2) * Fei_Lv2))
            c = float('%.2f' % (max(GongZhi_1, GongZhi_2) * Fei_Lv3))
            print('一次性工伤医疗补助金：', b, '元\n')
            print('一次性伤残就业补助金：', c, '元\n')   
        if SiFou_JieChu == 2:
            if DengJi == 4 or DengJi == 5:
                print('伤残津贴（每月）：',float('%.2f' % (GongZhi_1 * Fei_Lv4)),'元\n')
    elif (DengJi+1) <= 4:
        z = int(input('请输入生活自理障碍程度等级（数字）：'))
        z -= 1
        ShengHuoHuLiFei_DengJi_FeiLv = [0.6, 0.5, 0.4, 0.3]
        temp1 = float('%.2f' % (YuePing_GongZhi * ShengHuoHuLiFei_DengJi_FeiLv[z]))
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
    if (DengJi+1) > 4:
        if SiFou_JieChu == 1:
            print('\n以上待遇应发总额为：', float('%.2f' % (a + b + c + d + e + f)), '元')
            print('\n以上待遇补差总额为：', float('%.2f' % (a + b + c + d + e + g)), '元')
        if SiFou_JieChu == 2:
            print('\n以上待遇应发总额为：', float('%.2f' % (a + d + e + f)), '元')
            print('\n以上待遇补差总额为：', float('%.2f' % (a + d + e + g)), '元')
    if DengJi == 4 or DengJi == 5:
        print('\n以上待遇应发总额为（不含伤残津贴）：', float('%.2f' % (a + b + c + d + e + f)), '元')
        print('\n以上待遇补差总额为（不含伤残津贴）：', float('%.2f' % (a + b + c + d + e + g)), '元')
