import yagmail

yagmail.register('username', 'password')
yag = yagmail.SMTP('username@******.cn', host='mail.******.cn', port='465')

to = '138*******0@139.com'
subject = '邮件标题'
body = '邮件正文'

yag.send(to = to, subject = subject, contents = body)
