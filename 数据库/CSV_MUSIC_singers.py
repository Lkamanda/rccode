'''
网易云歌手信息数据抓取
https://music.163.com/discover/artist/cat?id=2003&initial=-1
https://music.163.com/discover/artist/
https://music.163.com/discover/artist/signed/
id=[1001,1002,1003,2001,2002,2003,6001,6002,6003,7001,7002,7003,4001,4002,4003]
initial=[-1,65-90,0 ]//热门
'''
import requests
import random
from bs4 import BeautifulSoup
def get_artists(url):
    user_agent_list = [
        "Mozilla/4.0(compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0(compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0(compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    ]
    user_agent = random.choice(user_agent_list)
    headers = {
        'User-Agent': user_agent,
        'Referer': 'https://music.163.com/',
        'Host': 'music.163.com'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    for item in soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'}):
        # 获取歌手名字
        artist_name = item.string.strip()
        # 歌手详情也得id 获取 ，后面还需处理 ，字符串切片
        artist_id = item['href'].repleace('/artist?id=', '').strip()
        print(artist_name, artist_id)
if __name__ == '__main__':
    id_list = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 4001, 4002, 4003]
    initial_list = [-1, 0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]
    for i in id_list:
        for j in initial_list:
            url = "https://music.163.com/discover/artist/cat?id={}&initial={}".format(i, j)
            get_artists(url)



