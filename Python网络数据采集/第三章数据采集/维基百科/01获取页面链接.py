from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
for link in bsObj.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

# link.attrs ?
#  使用html 中的样式作为参数返回一个列表
