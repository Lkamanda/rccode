import requests
from bs4 import BeautifulSoup
import random
import pymongo
def get_headers():
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
    return headers

def get_data(url):
    headers = get_headers()
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    movie_tables = soup.find_all('table', {"id": "tbContent"})[0].find_all('tr')[1:]
    #print(movie_tables)
    for movie in movie_tables:
        tds = movie.find_all('td')[1:]
        tds_title = movie.find_all('td')[0]
        movie_dict = {
            "movie_tile": tds_title.a.get('title'),
            "movie_href": tds_title.a.get('href'),
            "movie_type": tds[0].text,
            "box_office": tds[1].text,
            "average_fire": tds[2].text,
            "counties": tds[3].text,
            "movie_time": tds[4].text
        }
        movie_list.append(movie_dict)

def write_mongo(movie_list):
    client = pymongo.MongoClient('localhost')
    db_spider = client.spider
    movie_set = db_spider.movie_set
    movie_set.delete_many({})
    movie_set.insert_many(movie_list)

def main():
    global movie_dict
    global movie_list
    movie_list = []
    movie_dict = {}

    for n in range(2008, 2019):
        url = "http://www.cbooo.cn/year?year={}".format(n)
        get_data(url)
        a = len(movie_list)
        print(a)
    write_mongo(movie_list)




if __name__ == '__main__':
    main()