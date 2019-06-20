from urllib import request
import re
from bs4 import BeautifulSoup
url = "http://maoyan.com/board"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.ce1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
rsp = request.Request(url=url, headers=headers)
html = request.urlopen(rsp).read().decode()
print(html)
s = r'<dd>(.*?)</dd>'
# 非贪婪，s/匹配任何可见字符
pattern = re.compile(s, re.S)
movies = pattern.findall(html)
print(len(movies))
print(type(movies))

for film in movies:
    s = r'<a.*?href=".*?"'
    pattern = re.compile(s)
    title = pattern.findall(film)
    print(title)

