'''
https://tieba.baidu.com/f?
https://tieba.baidu.com/f?ie=utf-8&kw=%E9%87%91%E5%BA%B8&fr=search
'''

from urllib import request, parse
url = 'https://tieba.baidu.com/f?'
name = input("请输入贴吧名称:")
page = input("请输入贴吧页数:")
for i in range(int(page)):
    qs = {
        'kw': '金庸',
        'pn': i*50
    }

    qs_data = parse.urlencode(qs)
    url = url + qs_data
    print(url)