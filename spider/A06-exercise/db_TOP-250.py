import requests
import random
from bs4 import BeautifulSoup
import re
'''
https://movie.douban.com/top250?start=0&filter=
'''


def main():
    url = "https://movie.douban.com/top250?start=0&filter="
    headers = get_headers()
    soup = get_soup(url, headers)
    get_data(soup)


def get_headers():
    user_agent_list = [
        "Mozilla / 4.0(compatible;MSIE6.0;WindowsNT5.1;SV1;AcooBrowser;.NETCLR1.1.4322;.NETCLR2.0.50727)",
        "Mozilla/4.0(compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; "
        "Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0(compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; "
        ".NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 "
        "Safari/537.36"
    ]
    user_agent = random.choice(user_agent_list)
    headers = {
        "User-Agent": user_agent
    }
    return headers


def get_soup(url, headers):
    html = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    return soup


def get_data(soup):

    movie_list_soup = soup.find('ol', {'class': 'grid_view'})
    movie_data = []
    for movie_li in movie_list_soup.find_all('li'):

        movie_soup = movie_li.find('div', {'class': 'hd'}).find('a')
        href = movie_soup.get('href')

        movie_name = movie_soup.find('span', {'class': 'title'}).getText()
        movie_introduce = movie_li.find('div', {'class': 'bd'}).find('p').getText().replace(' ', '').replace('\n', '')
        movie_score = movie_li.find('span', {'class': 'rating_num'}).getText()
        movie_introduce_num = int(movie_li.find('div', {'class': 'star'}).find_all('span')[3].getText().split('人')[0])

        movie_quote = movie_li.find('p', {'class': 'quote'}).getText()
        movie_dict = {'movie_name': movie_name, 'href': href, 'movie_score': movie_score,
                      'movie_introduce': movie_introduce, 'movie_introduce_num': movie_introduce_num,
                      'movie_quote': movie_quote}
        movie_data.append(movie_dict)
    print(movie_data)


def getUrl_list(soup):
    url_list = soup.find_all('span', {'class': 'prev'})
    print(url_list)


if __name__ == '__main__':
    url = "https://movie.douban.com/top250?start=0&filter="
    headers = get_headers()
    soup = get_soup(url, headers=headers)
    getUrl_list(soup)



