import csv
import requests
import random
from lxml import etree
import re
url = 'http://www.seputu.com/'
user_agent_list = [
    "Mozilla/4.0(compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0(compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0(compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
]
user_agent = random.choice(user_agent_list)
headers = {
    "User-Agent": user_agent
}

req = requests.get(url, headers=headers)
# 使用etree解析html
html = etree.HTML(req.text)
div_mules = html.xpath('//*[@class="mulu"]')
rows = []
headers = ['标题', '小标题', '网址']
for div_mule in div_mules:
    div_h2 = div_mule.xpath('.//div[@class="mulu-title"]/center/h2/text()')

    if len(div_h2) > 0:
        # h2_title 小说总标题
        h2_title = div_h2[0]
        a_s = div_mule.xpath('.//div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0]
            box_title = str(a.xpath('./@title')[0]).split(']')[-1].strip(' ')
            date = str(a.xpath('./@title')[0]).split(']')[0].lstrip('[')
            # print(box_title)
            # print(type(box_title))
            # 数据集合
            content = (h2_title, box_title, href, date)
            print(content)
            rows.append(content)

            with open('盗墓笔记.cvs', 'w', newline='', encoding='utf-8-sig') as f:
                f_cvs = csv.writer(f)
                f_cvs.writerow(headers)
                f_cvs.writerows(rows)



