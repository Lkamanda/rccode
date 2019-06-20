from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
'''
ce1.他们都在id 为bodyContent中
2.URL链接不包含冒号
3.URL链接都在/wiki/开头
'''
html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")

bsObj = BeautifulSoup(html)
for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])

# Python通过re模块提供对正则表达式的支持。
# 使用re的一般步骤是先使用re.compile()函数，
# 将正则表达式的字符串形式编译为Pattern实例，
# 然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），
# 最后使用Match实例获得信息，进行其他的操作。

#   ^(/wiki/)((?!:).)*$
# ^ 正则开始        *$正则结束
# (?!) 字符串中不能包含的符号
