"""
喜马拉雅：https://www.ximalaya.com/
pypinyin包的使用，将汉子转换称拼音的包
"""

import requests
from pypinyin import lazy_pinyin
import random
import re
import json
from urllib import request


def get_headers():
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 '
        '(KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 '
        '(KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .N'
        'ET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) '
        'Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; '
        '.NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) '
        'QQBrowser/6.9.11079.201'
    ]
    user_agent = random.choice(user_agent_list)
    headers = {
        "User-Agent": user_agent
    }
    return headers


# 将输入的汉子转换成中文
def fanyi(pyin):
    var = lazy_pinyin(pyin)
    music_str = ''.join(var)
    return music_str


# 获取详情页面信息
def start_spider(str1, headers):
    url = 'https://www.ximalaya.com/yinyue/{}/'.format(str1)
    # 获取请求响应码
    # req_num = requests.get(url, headers=headers).status_code
    # print(req_num)
    html = requests.get(url, headers=headers).text
    return html


# 获取albumId    "albumId":412359,"title":"最新最火最好听流行歌曲"
def get_albumId(html):
    albumIds = re.findall(r'"albumId":(.*?),', html)
    print(albumIds)
    for albumId in albumIds:
        # 构建下载地址
        download_url = 'https://www.ximalaya.com/revision/play/album?albumId={}' \
                   '&pageNum=1&sort=-1&pageSize=30'.format(albumId)
        # 获取json
        # print(download_url)
        # print(headers)
        music_json = requests.get(url=download_url, headers=get_headers()).text
        download_music(music_json)


# 开始下载音乐
def download_music(music_json):
    # 获取下载音乐标题
    music_json = json.loads(music_json)
    #print(music_json)

    # 获取歌曲和下载链接
    titles = music_json['data']['tracksAudioPlay']

    # print(type(titles))
    # print(titles)
    for title in titles:
        title_name = title['trackName']
        title_url = title['src']
        if '/' in title_name:
            title_name = title_name.replace('/', '-')
        filename = "/Users/dxm/PycharmProjects/rccode/spider/A06-ERERCISE/喜马拉雅music/" + title_name + '.mp4'
        # 使用urllib库的request下载
        request.urlretrieve(url=title_url, filename=filename)


def main():
    music_type = input('please input you want listen music type:')
    headers = get_headers()
    str1 = fanyi(music_type)
    html = start_spider(str1, headers)
    get_albumId(html)


if __name__ == '__main__':
    main()




