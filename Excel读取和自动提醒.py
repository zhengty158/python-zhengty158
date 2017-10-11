# -*- coding: utf-8 -*-
import xlrd, yagmail

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
        break

def send_mail():
    # 如果有提醒，就自动发邮件到139邮箱，139邮箱收信后会免费发短信到手机
    print('\n\n第一次发邮件可能要手动输入密码\n\n')
    yagmail.register('username', 'password')
    yag = yagmail.SMTP('username@*******.cn', host='mail.******.cn', port='465')
    # 收件地址、标题、正文
    to = '138*******0@139.com'
    subject = '法律系统报错'
    body = '法律系统状态异常，请及时查看处理！'
    # 发送邮件
    yag.send(to = to, subject = subject, contents = body)
