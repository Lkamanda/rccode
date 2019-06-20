import pymongo
import requests
from bs4 import BeautifulSoup
import random
def get_data():
    all_movies_name = []
    all_movie_href = []
    all_movie_type = []
    all_boxoffice = []
    all_average_fare = []
    all_average_people = []
    all_counties = []
    all_date = []
    all_directorname = []
    for n in range(2008, 2018):
        print(n)
        url = "http://www.cbooo.cn/year?year={}".format(n)
        user_agent_list = [
            "Mozilla/4.0(compatible; MSIE 6.0; Windows NT 5.ce1; SV1; AcooBrowser; .NET CLR ce1.ce1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0(compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0(compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.ce1; .NET CLR ce1.ce1.4322; .NET CLR 2.0.50727)",
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
        for movie in movies:
            print(type(movie))



        movie_names = [tr.find_all('td')[0].a.get('title') for tr in movies[1:]]
        movie_href = [tr.find_all('td')[0].a.get('href') for tr in movies[1:]]
        movie_type = [tr.find_all('td')[1].string for tr in movies[1:]]
        boxoffice = [int(tr.find_all('td')[2].string) for tr in movies[1:]]
        average_fare = [int(tr.find_all('td')[3].string) for tr in movies[1:]]
        average_people = [int(tr.find_all('td')[4].string) for tr in movies[1:]]
        counties = [tr.find_all('td')[5].string for tr in movies[1:]]
        date = [tr.find_all('td')[6].string for tr in movies[1:]]
        director_name = [get_director(href, headers) for href in movie_href]

        for x in movie_names:
            all_movies_name.append(x)
        for x in movie_type:
            all_movie_type.append(x)
        for x in movie_href:
            all_movie_href.append(x)
        for x in boxoffice:
            all_boxoffice.append(x)
        for x in average_fare:
            all_average_fare.append(x)
        for x in average_people:
            all_average_people.append(x)
        for x in counties:
            all_counties.append(x)
        for x in date:
            all_date.append(x)
        for x in director_name:
            all_directorname.append(x)
    print(all_movie_href)
    print('数据写入')
    dates = {
        "name": all_movies_name,
        "href": all_movie_href,
        "总票房": all_boxoffice,
        "类型": all_movie_type,
        "平均票价": all_average_fare,
        "场均人数": all_average_people,
        "国家或地区": all_counties,
        "上映日期": all_date,
        "导演名": all_directorname
    }
    # print(dates)
    movies_set.insert()


def client_mongo(dates):
    client = pymongo.MongoClient()
    # 连接数据库，没有则创建
    db = client.movies
    # 连接集合，没有则创建
    movies_set = db.movies_set






def get_director(href, headers):
    req = requests.get(href, headers=headers)
    director_soup = BeautifulSoup(req.text, 'lxml')
    # print(director_soup)
    try:
        director = director_soup.select("dl.dltext dd")[1].p.a.get('title')
        # print(director)
    except:
        director = '不好意思没找到数据'

    return director

if __name__ == '__main__':
    try:
        client = pymongo.MongoClient()
        db = client.movie
        movies_set = db.movies_set
        get_data()
    except Exception as e:
        print(e)
