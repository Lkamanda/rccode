import requests
from bs4 import BeautifulSoup
from lxml import etree
import random
# 代码优化,将相同的操作封装成装饰器
import os

def mz_spider(base_url, headers):
    req = requests.get(base_url, headers=headers)
    html = etree.HTML(req.text)
    # 获取详情页信息
    img_src = html.xpath('//div[@class="postlist"]/ul/li/a/@href')
    for img_url in img_src:
        # 得到详情页的链接
        # print(img_url)
        # print("列表中有链接{}".format(len(img_src)))
        img_parse(img_url)


# 对详情页面的处理
def img_parse(img_url):
    headers={
        "User-Agent": user_agent,
        "Referer": "https://www.mzitu.com/"
    }
    req = requests.get(img_url, headers=headers)
    html = etree.HTML(req.text)

    # 获取图片标题
    title = html.xpath('//div[@class="content"]/h2/text()')[0]
    # print(title)

    # 获取图片一共有多少页码
    page_num = html.xpath('//div[@class="pagenavi"]/a/span/text()')[-2]
    #print(page_num)

    # 拼接详情页的n页链接地址
    for num in range(1, int(page_num)+1):
        img_src = img_url + "/" + str(num)
        #print(img_src)
        download_img(img_src, title)
# 下载图片
def download_img(img_src, title):
    req = requests.get(img_src)
    html = etree.HTML(req.text)

    # 图片的具体链接地址
    img_url = html.xpath('//div[@class="main-image"]/p/a/img/@src')[0]

    # 下载路径
    root_dir = 'mz_img'
    img_name = img_url.split('/')[-1]
    # print(img_name)
    title = title.replace(' ', '')
    # print(title)

    # 把存储路径和图片title 进行拼接   使其成为文件名
    root_dir = root_dir + "\\" + title
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
    res = requests.get(img_url, headers=headers)

    # 写入文件
    with open(root_dir + "\\" + img_name, 'wb') as f:
        f.write(res.content)
        f.close()
        print(title+"---" + img_name)

if __name__ == '__main__':
    pages = input("你想抓取多少页的图片:")
    start_url = "https://www.mzitu.com/"
    user_agent_list = [
        "Mozilla/4.0(compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0(compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0(compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    ]
    user_agent = random.choice(user_agent_list)
    # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
    headers = {
        "User-agent": user_agent,
        "Referer": "https://www.mzitu.com/"
    }

    # base_url = "https://www.mzitu.com/page/2/"
    # 妹子图
    for n in range(1, int(pages)):
        base_url = start_url + "page/" + str(n)
        print(base_url)
        mz_spider(base_url, headers)