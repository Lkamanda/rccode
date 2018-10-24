'''
使用selenium 爬取页面
保存内容使用xpath 进行解析
'''
from selenium import webdriver
from lxml import etree
import time
page = 0
url = "https://book.douban.com/subject_search?search_text=python&cat=1001&start=%s"% page
def get_web(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(4)
    driver.save_screenshot("豆瓣阅读.png")
    fn = 'douban_reader_html'
    with open(fn, 'w', encoding="utf-8") as f:
        # 把的到页面源码写入fn
        f.write(driver.page_source)
    content_parse(fn)
    driver.quit()

def content_parse(fn):
    html = ''
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()
    # 生成xml树
    tree = etree.HTML(html)

    # 查找书
    books = tree.xpath('//div[@class="item-root"]')
    for book in books:
        book_name = book.xpath('.//div[@class="title"]/a')
        print(book_name[0].text)
        book_href = book.xpath('.//div[@class="title"]/a/@href')
        print(book_href[0])
        #book_from = book.xpath('.//div[class="rating"]/div/@class="abstract"')
        #print(book_from[0].text)

def get_last(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_xpath("")

if __name__ == '__main__':
    get_web(url)

# 如何把全部数据取出
# false怎么解决
