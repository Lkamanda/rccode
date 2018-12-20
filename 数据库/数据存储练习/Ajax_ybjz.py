'''
Ajax异步加载

https://www.pexels.com/?
https://www.pexels.com/?dark=true&page=2
https://www.pexels.com/?dark=false&format=js&page=3&seed=2018-12-20+10:06:45++0000&format=js&seed=2018-12-20 10:06:45 +0000
https://www.pexels.com/?dark=true&format=js&page=4&seed=2018-12-20+10:06:45++0000&format=js&seed=2018-12-20 10:06:45 +0000
'''


import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": " Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
urls = ['https://www.pexels.com/?dark=true&page={}'.format(str(i)) for i in range(1,6)]
for url in urls:
    response = requests.get(url, headers=headers)
