import re, urllib.request as req

url = req.urlopen('http://************/')    # 获取网页源代码
data = url.read().decode('utf-8')            # 解码
keyword = 'blank">(.+)</a>'                  # 设置提取新闻的正则表达式
readlist = re.findall(keyword, data)         # 提取新闻

for n in range(len(readlist)):
    print(readlist[n])
