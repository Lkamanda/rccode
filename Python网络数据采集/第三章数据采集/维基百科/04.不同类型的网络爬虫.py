from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

page =set()
random.seed(datetime.datetime.now())

# 获取页面所有内链列表
def getInternalLinks(bsObj, includeUrl):
    # urlparse 把url 拆分成6个部分，
    # scheme(协议）,netloc(域名），path(路径），
    # params(可选参数），query(连接键值对)，fragment（特殊锚）
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
    # includerUrl = 协议：//域名
    # 创建空列表
    internalLinks = []
    # 找出所有以"/"开头的url
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            # 找到的链接不再列表里
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以"http" 或"www"开头且不包含当前URL的链接
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    # str.replace(old, new[,max]
    # 字符串新的内容被旧的替换, 可设置参数替换几次
    # str.split('指定字符', count)    对指定符串使用指定字符进行切割, count 为切割次数
    addressParts = address.replace("http://", "").split("/")
    return addressParts


