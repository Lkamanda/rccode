import requests

from lxml import etree
import random
from bs4 import BeautifulSoup
#start_url = "https://www.cnblogs.com/cate/python/"
# url = "https://www.cnblogs.com/cate/python/#p4"
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
def spider_sdn(headers, page_num):
    url = "https://www.cnblogs.com/cate/python/#p%s" % page_num
    print(url)
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    items = soup.select('div[class="post_item_body"]')
    for item in items:
        # title 每个帖子下的标题
        title = item.select('h3 a[class="titlelnk"]')[0].get_text()
        # href 帖子链接
        href = item.select('h3 a[class="titlelnk"]')[0]['href']
        # author 帖子作者
        #aut = item.select('div a[class="lightblue"]')[0].get_text()
        # time 贴发表时间
        time = item.select('div[class="post_item_foot"]')[0].get_text().strip(' ').strip('\n')
        #print(time)
        time = time.split(' ')
        # print(len(time))
        # 发布时间
        aut1 = time[0]
        print(aut1)
        time_1 = str(time[6]) + ' '+str(time[7])
        print(time_1)
        # comment 评论数  readnum
        # commentnum_readnum = time[-1]
        # 评论(0)阅读(1)
        pinglun = time[-1].lstrip('评论(').rstrip(')')[0]
        read_num = time[-1].lstrip('评论(').rstrip(')').split('(')[-1]
        print(pinglun)
        print(read_num)
        read_num = time[-1].strip('')
        aut_href = item.select('div a[class="lightblue"]')[0].get('href')
        # content 贴子内容简介
        content = item.select('p[class="post_item_summary"]')[0].get_text().strip('\n').strip(' ')
        #print(content)
def getUrl(page_num):
    for i in range(1, page_num):
        spider_sdn(headers=headers, page_num=i)
        print(i)

if __name__ == '__main__':
    page_num = int(input('请输入想获取信息的页数:'))
    page_num = page_num + 1
    # spider_sdn(url, headers)
    getUrl(page_num)
