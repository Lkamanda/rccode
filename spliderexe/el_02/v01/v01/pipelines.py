# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class V01Pipeline(object):
    def process_item(self, item, spider):
        '''
        此案例制式把item 值打印出来
        :param item:
        :param spider:
        :return:
        '''
        with open('meiju.json', 'a') as f:
            json.dump(dict(item), f)
        return item

