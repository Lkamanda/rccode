import scrapy
from v01.items import V01Item

class MejuSpider(scrapy.Spider):
    name = "meiju"
    start_urls = ['http://www.meijutt.com/new100.html']

    # 重写parse
    def parse(self, response):
        '''
        默认已经得到页面
        反馈内容用response表示
        其中包含需要的所有数据
        :param response:
        :return:
        '''
        # 通过xpath 能找到所有电影
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        print("moives len{0}".format(len(movies)))
        for movie in movies:
            '''
            每个movie都需要转换成一个item
            '''
            item = V01Item()
            item['name'] = movie.xpath('./h5/a/@title').extract()[0]
            item['href'] = movie.xpath('./h5/a/@href').extract()[0]

            # tv 属性肯能有问题
            tv = movie.xpath('./span[@class="mjtv"]/text()')
            if len(tv):
                item['tv'] = tv.extract()[0]
            else:
                item['tv'] = ""
            print('item.name:{0}'.format(item['name']))
            # item需要返回yield
            yield item
