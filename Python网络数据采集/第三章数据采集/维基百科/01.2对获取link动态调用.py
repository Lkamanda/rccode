'''
ce1.缺少对异常的处理
    - 别入 bodyContent 标签名称改变
    - 网络状态的各种处理
2. 对获取数据的储存和分析
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# 伪随机,所产生随机数很难预测,且呈均匀分布,耗费cpu资源

# 使用系统当前时间生成一个随机数的生成器,保证每次程序运行时,维基百科选择都是全新的随机路径
random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    # 使用字符串拼 参数和原网站 生成新的url
    html = urlopen("https://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    # 使用正则抽取标签a 并返回
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)






