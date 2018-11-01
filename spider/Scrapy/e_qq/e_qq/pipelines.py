# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class EQqPipeline(object):
    def process_item(self, item, spider):
        return item
class QQPipeline(object):
    '''
    假定数据需要写如文件
    name在什么时候,打开文件
    '''
    def __init__(self):
        self.file = open('qq.json, spider', 'wb')
        print("写入文件")

    def process_item(self, item, spider):
        # item 可以直接转化成字典
        content = json.dumps(dict(item), ensure_ascil=False) +'\n'
        self.file.write(content)

        return item
    def close_spider(self, spider):
        self.file.close()
        print('关闭文件')
