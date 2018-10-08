from bs4 import BeautifulSoup
from urllib.request import urlopen

html= urlopen("http://www.pythonscraping.com/pages/page3.html")

bsObj = BeautifulSoup(html)

#for child in bsObj.find("table", {"id":"giftList"}).children:
    #print(child)

a = bsObj.table.tr.previous_siblings
print(a)
for siblings in bsObj .find("table",{"id":"giftList"}).tr.next_siblings:
    print(siblings)
