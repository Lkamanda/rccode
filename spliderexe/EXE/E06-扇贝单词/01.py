from urllib import request
from lxml import etree
import json

def shanbei(page):
    url ="https://www.shanbay.com/wordlist/187711/540709/?page=%s" % page
    rsp = request.urlopen(url)
    html = rsp.read()
    html = etree.HTML(html)
    tr_list = html.xpath("//tr")
    for tr in tr_list:
        word = {}
        #strong = tr_list.xpath('./td[@class="span2"]')
        strong = tr.xpath('.//strong')
        if len(strong):
            name = strong[0].text.strip()
            word['name'] = name
            #print(name)
        td_content = tr.xpath('./td[@class="span10"]')
        if len(td_content):
            content = td_content[0].text.strip()
            word['content'] = content
            #print(content)
        print(word)
if __name__ == '__main__':
    for i in range(9):
        shanbei(i)