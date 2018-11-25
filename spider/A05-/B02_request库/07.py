import requests
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
url_list = []
n = 0
x = 13
def getUrl(url):
    global n, x
    driver = webdriver.Chrome()

    driver.get(url)
    driver.find_element_by_xpath('//*[@id="paging_block"]/div/a[%s]' % x).click()
    if x < 14:
        x += 1
    sleep(3)
    url = driver.current_url
    print(url)
    driver.close()
    n = n + 1
    if n < 3:
        getUrl(url)


def spider(url):
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
    req = requests.get(url=url, headers=headers)

    soup = BeautifulSoup ( req.text, 'lxml')
    items = soup.select ( 'div[class="post_item_body"]' )
    for item in items:
        # title 每个帖子下的标题
        title = item.select ( 'h3 a[class="titlelnk"]' )[ 0 ].get_text ()

if __name__ == '__main__':
    url = "https://www.cnblogs.com/cate/python/"
    getUrl(url)



#
#
# page_num = int(input('qing:'))
# page_num = page_num + 1
# for i in range(1, page_num):
#     url = "https://www.cnblogs.com/cate/python/#p%s" % i
