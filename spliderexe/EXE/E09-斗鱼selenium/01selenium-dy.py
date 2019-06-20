'''
任务:爬取斗鱼直播内容
https://www.douyu.com/directory/all
思路
ce1.利用selenium得到页面内容
2.利用xpath 或者bs 等在页面中进行信息提取
'''

from selenium import webdriver
from bs4 import BeautifulSoup
class Douyu():
    # 初始化
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.douyu.com/directory/all'
    def douyu(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(4)
        while True:
            soup = BeautifulSoup(self.driver.page_source, 'xml')
            # 返回当前页面所有标题列表和人数
            titles = soup.find_all('h3', {'class': 'ellipsis'})
            nums = soup.find_all('span', {'class': 'dy-num fr'})
            for title, num in zip(titles, nums):
                print("房间{0}总共有人数{1}".format(title.get_text().strip(), num.get_text().strip()))

    def destr(self):
        self.driver.quit()

if __name__ == '__main__':
    # 生成一个类实例
    douyu = Douyu()
    douyu.setUp()
    douyu.douyu()
    douyu.destr()
