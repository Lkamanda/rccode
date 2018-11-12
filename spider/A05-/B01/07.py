from urllib import request, parse
from lxml import etree
import os
import json
url = "http://zuihaodaxue.com/zuihaodaxuepaiming2018.html"

req = request.Request(url=url)

response = request.urlopen(req)
html = response.read().decode()
# 使用etree 对 获取的html 进行处理
html = etree.HTML(html)
items = html.xpath('//tr[@class="alt"]')
for item in items:
    # 排名
    num_1 = item.xpath('./td')[0].text
    #print(num_1)
    # 学校名称
    school_name = item.xpath('.//div[@align="left"]')[0].text
    #print(school_name)
    # 省份
    province = item.xpath('./td')[2].text
    #print(province)
    # 总分
    score_1 = item.xpath('./td')[3].text
    #print(score_1)
    # 指标分
    score_2 = item.xpath('./td')[4].text
    #print(score_2)
    #print(num_1+"__"+ school_name+"__"+province+"__"+score_1+"__"+score_2)
    filename = r"data.txt"
    a = [num_1, school_name, province, score_1, score_2]
    #print(a)
    #os.remove(filename)
    with open(filename, 'a+', encoding="utf-8") as f:
        f.write(json.dumps(a, ensure_ascii=False))
