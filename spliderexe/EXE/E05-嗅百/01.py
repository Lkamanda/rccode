'''
爬去嗅百
1.需要用到requests爬取页面，用xpath.re来提取数字
2.可以获取用户链接，段子内容。点赞好评次数
3.保存到json格式

大致分为三步
1.down下页面
2.利用xpath提取信息
3.保存文件落地
'''
import requests
from lxml import etree
url = "https://www.qiushibaike.com/"
headers = {
    "User-Agent": "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"
}
#下载页面
rsp = requests.get(url, headers=headers)
html = rsp.text
# 把页面解析成html
html = etree.HTML(html)
# contains(@)
rst = html.xpath('//div[contains(@id, "qiushi_tag")]')

for r in rst:
    item = {}
    # 转换成文本,去掉空格
    content = r.xpath('//div[@class="content"]/span')[0].text.strip()
print(content)