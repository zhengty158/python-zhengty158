# 该代码用于爬取视频合集中某一个歌手的所有视频，并随机播放
# coding = utf-8
import re, urllib.request as req, random, webbrowser, gzip
from io import BytesIO

# 获取该视频合集网页源码
url = req.urlopen('http://www.bilibili.com/video/av3290650')
data = url.read()

# 解决报错问题：'utf-8' codec can't decode byte 0x8b in position 1
buff = BytesIO(data) # 把data转为文件对象
f = gzip.GzipFile(fileobj=buff)
res = f.read().decode('utf-8')

# 提取指定歌手的所有视频
key = '<option value=\'/video/av3290650/index_(.+).html\' cid=\'.+\'>(.*(如月千早|今井麻美).*)</option>'
read = re.findall(key, res)
playlist = list(range(1, len(read)))

# 随机抽取某一个该歌手的视频播放
while True:
    playchoice = random.sample(playlist, 1)
    webbrowser.open_new_tab('http://www.bilibili.com/video/av3290650/index_{number}.html'.format(number = read[playchoice[0]][0]))
    input('继续.....')

