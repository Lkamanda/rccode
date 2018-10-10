from bs4 import BeautifulSoup
from urllib.request import urlopen
# from urllib import response
import re
import time
import socket
# socket.setdefaulttimeout(20)
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org/"+pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a", href=re.compile("(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                #time.sleep(10)
                # response.close()
                getLinks(newPage)

getLinks("")