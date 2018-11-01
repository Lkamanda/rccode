# requests
import requests
newsurl = "https://www.sina.com.cn/"
res = requests.get(newsurl)
res.encoding = "utf-8"
print(res.encoding)
# 把回应的方法取出
print(res.text)

#with open("sina.text", "w") as f:
    #for i in res.text:
           # f.write(i)


# bs4
from bs4 import BeautifulSoup
html_sample= ""
soup = BeautifulSoup(html_sample, 'html.parser')
# 把文本取出去掉标签
soup.text()
