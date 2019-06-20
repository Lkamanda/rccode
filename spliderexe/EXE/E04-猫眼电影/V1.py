'''
利用正则来爬取猫眼电影
ce1.url :http://maoyan.com/board
2.把电影信息尽可能的拿下来

# 分析
ce1. 一个影片的内容就是以一个dd开头的单元
2.对应找到的每一个dd,用re挨个查找需要的信息

# 方法就是散步走:
ce1.把页面down下来
2.提取出dd单元的内容
3.对每一个dd,进行单独的信息提取
'''

from urllib import request,parse
def getHtml():
    # ce1.下载页面内容
    url = "http://maoyan.com/board"

    rsp = request.urlopen(url)

    html = rsp.read().decode()

    print(html)

# 2.按dd提取出内容来,缩小处理范围

# s = r.<dd>