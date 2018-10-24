from bs4 import BeautifulSoup
from urllib import request

def tc(page):
    # 获取页面
    url = "https://hr.tencent.com/position.php?&start=%s0#a" % page
    rsp = request.urlopen(url)
    html = rsp.read()
    # 提取数据
    soup = BeautifulSoup(html, 'lxml')

    # 创建css选择器,得到相应的tags
    tr1 = soup.select("tr[class='even']")
    tr2 = soup.select("tr[class='even']")
    trs = tr1+tr2
    for tr in trs:
        name = tr.select('td a')[0].get_text()
        print(name)
        href = tr.select('td a')[0].attrs['href']
        print(href)
        count1 = tr.select('td')[2].get_text()
        print(count1)
# 统计我一共得到多少条数据

if __name__ == '__main__':
    for i in range(1):
        tc(i)