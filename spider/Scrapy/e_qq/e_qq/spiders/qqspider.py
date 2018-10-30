import scrapy
import re
from e_qq.items import QQItem

class QQSpider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['hr.tencent.com']
    start_urls = [
        'https://hr.tencent.com/position.php/position.php?&start=0#a'
    ]


    def parse(self, response):
        # 下载的结果自动放在response内存储
        for each in response.xpath('//*[class="even"]'):
            # 对于得到的每一个工作信息内容
            # 把数据封装日响应的item内
            item = QQItem()
            name = each.xpath('./td[1]/a/text()').extract()[0]
            detailLink = each.xpath('./td[1]/a/@href').extract()[0]
            positionInfo = each.xpath('./td[2]/text()').extract()[0]
            workLocation = each.xpath('./td[4]/text()').extract()[0]


            item['name'] = name.encode('utf-8')
            item['detailLink'] = detailLink.encode('utf-8')
            item['positionInfo'] = positionInfo.encode('utf-8')
            item['workLocation'] = workLocation.encode('utf-8')
            # 处理继续爬取的链接
            # 通过得到当前页,提取数字,数字加10 ,替换原来的数字,就是是下一个页面地址
            curpage = re.search('(\d+)', response.url).group(1)
            page = int(curpage) + 10
            # 生成下一页url
            url = re.sub('\d+', str(page), response.url)
            # 把地址通过携程放回
            print(url)
            yield scrapy.Request(url, callback=self.parse)

            # 把获取的item提取交给pipeline
            yield item
