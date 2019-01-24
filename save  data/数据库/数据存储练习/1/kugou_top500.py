'''
https://www.kugou.com/yy/rank/home/1-8888.html?from=rank
'''
import requests
from bs4 import BeautifulSoup
import random
import pymongo



def get_dates(url, i):
    print("@@@@@{}!!!!!!".format(i))
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
    ranks = soup.select('.pc_temp_num')
    sing_names = soup.select('.pc_temp_songlist > ul > li > a ')

    sing_times = soup.select('.pc_temp_time')

    for rank, sing_name, sing_time in zip(ranks, sing_names, sing_times):
        # 歌曲排名
        rank = rank.get_text().strip()
        #print(rank, type(rank))

        sing = sing_name.get_text()
        # 歌手姓名
        sing_name = sing.split('-')[-1].strip()
        # 歌曲信息
        singer_name = sing.split('-')[-0].strip()
        # 歌曲时间
        sing_time = sing_time.get_text().strip()
        # print(rank, sing_name, singer_name, sing_time)
        # my_set.insert({'rank': rank, 'sing_name': sing_name, 'sing_time': sing_time})
        datas = {'rank': rank, 'sing_name': sing_name, 'sing_time': sing_time}
        print(datas, type(datas))



if __name__ == '__main__':
    for i in range(1, 20):
        url = "https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank".format(i)
        get_dates(url, i)