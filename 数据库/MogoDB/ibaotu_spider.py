"""
对：https://ibaotu.com/shipin/7-0-0-0-0-3.html
进行抓去
"""
from agent import get_User_agent
# from mongo_api import MongoAPI
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


class Spider(object):
    def __init__(self):
        self.headers = {
            "User-Agent": get_User_agent()
        }
        self.offset = 1
        self.video_dates = []
        self.video_id = 0

    # 主函数
    def main_func(self):
        for i in range(1, 200):
            url = "https://ibaotu.com/shipin/7-0-0-0-0-{}.html".format(i)
            self.get_request(url)
        print(self.video_dates)
        self.video_mongo(self.video_dates)

    # mongo写入
    def video_mongo(self, video_dates):
        conn = MongoClient()
        video_db = conn.spider
        video_set = video_db.video_set
        video_set.insert_many(video_dates)

    # 获取数据

    def get_request(self, url):
        req = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(req.text, 'lxml')
        video = soup.find_all('div', {'class': 'media-list'})[0]
        video_list = video.find_all('ul', {'class': 'clearfix'})[0].find_all('li')

        for video in video_list:
            video_div = video.find_all('div', {'class': 'video-titbox'})[0]
            video_href = video_div.find_all('a')[0].get('href')
            video_href = "https:" + video_href
            video_name = video_div.find_all('span', {'class': 'video-title'})[0].text
            self.video_id += 1
            print(self.video_id)
            video_dict = {'video_id': self.video_id, 'video_name': video_name, 'video_href': video_href}
            self.video_dates.append(video_dict)


if __name__ == '__main__':
    spider = Spider()
    spider.main_func()


