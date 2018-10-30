'''
需要导入scrapy
所有类一般xxxSpider
所有爬虫scrapy.Spider的子类

'''
import scrapy
class BaiduSpider(scrapy.Spider):
    # name 是爬虫的名
    name = 'baidu'
    # 起始url列表
    start_urls = ['http://www.baidu.com']
    # 负责downloader 下载的到的结果
    def parse(self, response):
        '''
        只是保存网页即可
        :param reponse:
        :return:
        '''
        with open('baidu.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode('utf-8'))


