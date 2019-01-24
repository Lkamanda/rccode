# 利用pandas保存数据
# 抓去中国票房网站的数据

import pandas
import requests
from bs4 import BeautifulSoup
import random
import csv
daoyan_url_list =[]
def get_fp(url, n):
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
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    movies_table = soup.find_all('table', {'id': 'tbContent'})[0]
    movies = movies_table.find_all('tr')
    # names = [tr.find_all('td')[0].a.get('title') for tr in movies[1:]]
    # print(names)
    # print(movies[0])
    # 参数标题获取
    if n == int('2008'):
        t1 = movies[0].find_all('th')[0].text
        t2 = movies[0].find_all('th')[1].text
        t3 = movies[0].find_all('th')[2].text
        t4 = movies[0].find_all('th')[3].text
        t5 = movies[0].find_all('th')[4].text
        t6 = movies[0].find_all('th')[5].text
        t7 = movies[0].find_all('th')[6].text
        t8 = 'href'
        t9 = '导演'
        print(t1, t2, t3, t4, t5, t6, t7, t8)
        try:
            writer.writerow((t1, t2, t3, t4, t5, t6, t7, t8, t9))
        except Exception as e:
            print('写入标题失败')
            print(e)

    for tr in movies[1:]:
        names = tr.find_all('td')[0].a.get('title')
        movie_type = tr.find_all('td')[1].text
        pf = tr.find_all('td')[2].text
        c_jun_jia = tr.find_all('td')[3].text
        c_jun_ren = tr.find_all('td')[4].text
        country = tr.find_all('td')[5].text
        movie_start_date = tr.find_all('td')[6].text
        movie_href = tr.find_all('td')[0].a.get('href')
        daoyan_url_list.append(movie_href)
        for href in daoyan_url_list:
            data = requests.get(href)
            soup = BeautifulSoup(data.text, 'lxml')
            # director_name = soup.find_all('dl', {'class': 'dltext'})[0].find_all('dd')[0].a.get('title')
            director_name = soup.select('dl.dltext dd')[1].a.get_text()

        print(names, movie_type, pf, c_jun_jia, c_jun_ren, country, movie_start_date, movie_href, director_name)
        try:
            writer.writerow((names, movie_type, pf, c_jun_jia, c_jun_ren, country, movie_start_date, movie_href,
                             director_name))
        except Exception as e:
            print('数据写入失败')
            print(e)



if __name__ == '__main__':
    with open('中国票房网爬虫.csv', 'a', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        for n in range(2008, 2009):
            print(n)
            url = 'http://www.cbooo.cn/year?year={}'.format(n)
            get_fp(url, n)