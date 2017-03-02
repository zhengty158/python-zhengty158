# -*- coding: utf-8 -*-
# 办公小工具：用Python调用Windows命令行，实现批量查找文件、删除文件功能
# 自我感觉比Windows的bat（批处理）文件好用多了，不用每次都手动右键替换查询关键字和盘符，哈哈！顺便练练面向对象编程。

import os

class WIN_DIR_DEL(object):

    CMD_dir = 'dir %s:\*%s /a/s/p >c:\\文件查找结果-%s.txt'  # WIN命令行的文件查找命令，>号后面是存放路径，用于存放查找结果
    CMD_del = 'del %s:\*%s /a/s/p'                          # WIN命令行的文件删除命令，/a/s/p分别代表：查找所有属性的文件/查找所有子文件夹/每删除一个文件都需要手动确认
    All_PanFu = ['c', 'd', 'e', 'f']                        # WIN系统常见硬盘盘符

    # 以下函数为文件查找命令
    def WIN_dir(self):
        
        PanFu = input('\n请问要在哪个或哪些硬盘中查找文件（比如：c 或cde）\n如果是所有硬盘，请输入：s\n> ')
        WenJianMin = input('\n请输入要查找的文件名（比如：通知）\n如果针对某一类文件（比如：pdf），请输入文件名后缀（比如：.pdf）\n> ')
        print('\n正在查找……\n')
        
        if '.' not in WenJianMin:
            WenJianMin += '*'
            if 's' in PanFu:
                for PanFu_New in WIN_DIR_DEL.All_PanFu:
                    os.system(WIN_DIR_DEL.CMD_dir % (PanFu_New, WenJianMin, PanFu_New))
            elif len(PanFu) >= 2:
                for PanFu_New in PanFu:
                    os.system(WIN_DIR_DEL.CMD_dir % (PanFu_New, WenJianMin, PanFu_New))
            else:
                os.system(WIN_DIR_DEL.CMD_dir % (PanFu, WenJianMin, PanFu))
                
        elif '.' in WenJianMin:
            if 's' in PanFu:
                for PanFu_New in WIN_DIR_DEL.All_PanFu:
                    os.system(WIN_DIR_DEL.CMD_dir % (PanFu_New, WenJianMin, PanFu_New))
            elif len(PanFu) >= 2:
                for PanFu_New in PanFu:
                    os.system(WIN_DIR_DEL.CMD_dir % (PanFu_New, WenJianMin, PanFu_New))
            else:
                os.system(WIN_DIR_DEL.CMD_dir % (PanFu, WenJianMin, PanFu))
            
        print('\n查找完成，可以到C盘查看《文件查找结果》\n如果没找到，C盘不会生成《文件查找结果》')


    # 以下函数为文件删除命令
    def WIN_del(self):
        
        PanFu = input('\n请问要在哪个或哪些硬盘中删除文件（比如：c 或cde）\n如果是所有硬盘，请输入：s\n> ')
        WenJianMin = input('\n请输入要删除的文件名（比如：通知）\n如果针对某一类文件（比如：pdf），请输入文件名后缀（比如：.pdf）\n> ')
        print('\n正在查找……\n')
        
        if '.' not in WenJianMin:
            WenJianMin += '*'
            if 's' in PanFu:
                for PanFu_New in WIN_DIR_DEL.All_PanFu:
                    os.system(WIN_DIR_DEL.CMD_del % (PanFu_New, WenJianMin))
            elif len(PanFu) >= 2:
                for PanFu_New in PanFu:
                    os.system(WIN_DIR_DEL.CMD_del % (PanFu_New, WenJianMin))
            else:
                os.system(WIN_DIR_DEL.CMD_del % (PanFu, WenJianMin))

        elif '.' in WenJianMin:
            if 's' in PanFu:
                for PanFu_New in WIN_DIR_DEL.All_PanFu:
                    os.system(WIN_DIR_DEL.CMD_del % (PanFu_New, WenJianMin))
            elif len(PanFu) >= 2:
                for PanFu_New in PanFu:
                    os.system(WIN_DIR_DEL.CMD_del % (PanFu_New, WenJianMin))
            else:
                os.system(WIN_DIR_DEL.CMD_del % (PanFu, WenJianMin))

        input('\n删除完毕，按回车键退出')


    def run(self):
        print('\n\n        办公小工具：批量查找、删除文件\n\n')
        choice = int(input('查找文件请按1，删除文件请按2\n> '))
        if choice == 1:
            WIN_DIR_DEL().WIN_dir()
            for x in WIN_DIR_DEL().All_PanFu:                  # 按顺序自动打开每一个《文件查找结果》.txt
                os.system('c:\\文件查找结果-%s.txt' % x)
                input('\n按回车键查看下一个《文件查找结果》')
                if x == list(WIN_DIR_DEL().All_PanFu)[-1]:
                    input('\n按回车键退出')
        elif choice == 2:
            WIN_DIR_DEL().WIN_del()

WIN_DIR_DEL().run()
