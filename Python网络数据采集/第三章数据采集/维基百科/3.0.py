from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html)
    try:
        print(bsObj.get_text())
        print(bsObj.find(id="mv-content-text").findall("p"[0]))

    except AttributeError:
        print("页面缺少一些属性!不过不用担心!")
    for links in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in links.attr:
            if links.attr['href'] not in pages:
                newPage = links.attrs['href']
                print("----\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")
