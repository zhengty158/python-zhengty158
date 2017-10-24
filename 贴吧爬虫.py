# 贴吧爬虫，以爬取某贴吧首页置顶漫画更新情况为例
import urllib.request as req, yagmail, random, time
from bs4 import BeautifulSoup as Soup

# 找到更新的漫画就发邮件通知
def send_mail(num):
    yagmail.register('username', 'password')
    yag = yagmail.SMTP('***@********.cn', host='mail.********.cn', port='465')
    yag.send(to = '138*******0@139.com', subject = '漫画已更新到:%s话' % num, contents = '漫画已更新')
    
def search(num):
    # 抓取贴吧首页源码
    html = req.urlopen('https://tieba.baidu.com/f?kw=%E5%89%91%E9%A3%8E%E4%BC%A0%E5%A5%87')
    html_read = html.read().decode('utf-8')
    soup = Soup(html_read, 'html.parser')
    # 筛选关键词
    for x in soup.stripped_strings:
        if ('第' + num + '话') in x:
            print(x)
            return num
    
# 这是现在要等的最新一话
episode_num = 352

while True:
    result = search(str(episode_num))
    if result is not None:
        send_mail(str(episode_num))
        episode_num += 1
    wait_time = random.randint(43200, 72000)
    print('\n\n不要关闭本程序\n\n下次抓取时间为{time}小时后\n\n'.format(time = round(wait_time / 3600, 1)))
    time.sleep(wait_time)
