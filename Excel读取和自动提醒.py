# -*- coding: utf-8 -*-
import xlrd

# 可用于理财到期日的自动提醒
data = xlrd.open_workbook(excel_file)

table = data.sheets()[0]   #通过索引顺序获取
table = data.sheet_by_index(0)   #通过索引顺序获取
table = data.sheet_by_name(u'Sheet1')   #通过名称获取

# 第一行：table.row_values(0)
# 第一列：table.col_values(0)

# 获取某一列的全部数据
col_list = []
for x in table.col_values(9):
    col_list.append(x)

# 发现有Excel的自动提醒，就自动发邮件到用户的139邮箱，利用免费短信
for y in col_list:
    if '提醒' not in str(y):
        pass
    elif '提醒' in str(y):
        # 后面就是自动发邮件了
