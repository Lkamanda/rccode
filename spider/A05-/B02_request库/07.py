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
            # href 帖子链接
            href = item.select('h3 a[class="titlelnk"]')[0]['href']
            # author 帖子作者
            # aut = item.select('div a[class="lightblue"]')[0].get_text()
            # time 贴发表时间
            time = item.select('div[class="post_item_foot"]')[0].get_text().strip(' ').strip('\n')
            # print(time)
            time = time.split(' ')
            # print(len(time))
            # 发布时间
            aut1 = time[0]
            print(aut1)
            time_1 = str(time[6]) + ' ' + str(time[ 7 ])
            print(time_1)
            # comment 评论数  readnum
            # commentnum_readnum = time[-ce1]
            # 评论(0)阅读(ce1)
            pinglun = time[-1].lstrip('评论(').rstrip(')')[0]
            read_num = time[-1].lstrip('评论(').rstrip(')').split('(')[-1]
            print(pinglun)
            print(read_num)
            read_num = time[-1].strip('')
            aut_href = item.select('div a[class="lightblue"]')[0].get('href')
            # content 贴子内容简介
            content = item.select('p[class="post_item_summary"]')[0].get_text().strip('\n').strip(' ')
            # print(content)
if __name__ == '__main__':
    page_num = int(input('请输入你想查询信息的页数:'))
    sdn = Sdn()
    sdn.setUp()
    sdn.getUrl(page_num)
    sdn.sdn_close()





