from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(articalUrl):
    html = urlopen("https://en.wikipedia.org" + articalUrl)
    bsObj = BeautifulSoup(html, "lxml")
    # 获取维基百科内的id 属性为 bodyContent的下的所有链接
    # ？！ 正则内不能存在的字符串
    # .匹配任何字符串
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPS(pageUrl):
    # 编辑历史页面的url链接格式
    # https://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    #Programming_paradigm
    #https://en.wikipedia.org/w/index.php?title=Programming_paradigm&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "https://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    # 找出class="mw-userlink mw-anonuserlink" 的链接
    # 他们用ip地址代替用户名
    ipAddresses = bsObj.findAll("a", "{class:mw-userlink mw-anonuserlink")
    # 使用集合去重
    addressList = set()
    for ipaddress in  ipAddresses:
        addressList.add(ipaddress.get_text())
    return addressList

links = getLinks("/wiki/Python_(programming_language)")
while(len(links) > 0):
    for link in links:
        print('---------')

        historyIPS = getHistoryIPS(link.attrs["href"])
        for historyIP in historyIPS:
            print(historyIP)
    newlink = links[random.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newlink)