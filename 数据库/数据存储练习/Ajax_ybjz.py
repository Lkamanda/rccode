'''
Ajax异步加载

https://www.pexels.com/?
https://www.pexels.com/?dark=true&page=2
https://www.pexels.com/?dark=false&format=js&page=3&seed=2018-12-20+10:06:45++0000&format=js&seed=2018-12-20 10:06:45 +0000
https://www.pexels.com/?dark=true&format=js&page=4&seed=2018-12-20+10:06:45++0000&format=js&seed=2018-12-20 10:06:45 +0000
'''


import requests
from bs4 import BeautifulSoup
import re
import lxml

headers = {
    "User-Agent": "Mozilla/4.0(compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727"
}
urls = ['https://www.pexels.com/?dark=true&page={}'.format(str(i)) for i in range(1, 6)]
photos = []
for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    imgs = soup.select('artical > a > img')
    for img in imgs:
        photo = img.get('src')
        if photo.endswith('350'):
            photos.append(photo)
            print(photo)

path = r'C:\Users\v_zhoujialin_dxm\PycharmProjects\rccode\数据库\数据存储练习\img'
for item in photos:
    data = requests.get(item, headers=headers)
    photo_name = re.findall('\d+\/(.*?)\?',item)
    # print(photo_name[0])
    if photo_name:
        with open(path+"/"+photo_name[0],'wb') as f:
            f.write(data.content)

