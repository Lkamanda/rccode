# 使用selenium 对sdn 进行爬取
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
url_list = []
n = 0
x = 13

class Sdn():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.cnblogs.com/cate/python/"
        self.driver.get(self.url)
    def getUrl(self, page_num):
        global n, x
        sleep(5)
        Sdn.spider(self)
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="paging_block"]/div/a[%s]' % x).click()
        if x < 14:
             x += 1
        n = n + 1
        if n < page_num:
            Sdn.getUrl(self, page_num)

    def sdn_close(self):
        self.driver.close()
    def spider(self):
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        items = soup.select('div[class="post_item_body"]')
        for item in items:
            # title 每个帖子下的标题
            title = item.select('h3 a[class="titlelnk"]')[0].get_text()
            print(title)
if __name__ == '__main__':
    page_num = int(input('请输入你想查询信息的页数:'))
    sdn = Sdn()
    sdn.setUp()
    sdn.getUrl(page_num)
    sdn.sdn_close()





