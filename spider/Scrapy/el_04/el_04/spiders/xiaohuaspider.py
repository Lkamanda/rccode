import scrapy
from urllib import request
from el_04.items import XiaohuaItem

class XiaohuaSpider(scrapy.Spider):

    name = 'xiaohua'
    # 允许爬取的域名
    allowed_domain = ['']
    # 爬虫起始url
    start_urls = ['']
    def parse(self, response):
        bookmarks = response.xpath('')
        for bm in bookmarks:
            item = XiaohuaItem()

            title = bm.xpath('').extract()[0]

            item['title'] = title

            # 生成新的url 并返回
            yield url
            yield item

