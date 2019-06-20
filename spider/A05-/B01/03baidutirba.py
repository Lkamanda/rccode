'''
https://tieba.baidu.com/f?
https://tieba.baidu.com/f?ie=utf-8&kw=%E9%87%91%E5%BA%B8&fr=search
'''

from urllib import request, parse
import random
url = 'https://tieba.baidu.com/f?'
name = input("请输入贴吧名称:")
page = input("请输入贴吧页数:")
for i in range(int(page)):
    qs = {
        'kw': name,
        'pn': i*50
    }

    qs_data = parse.urlencode(qs)
    url = url + qs_data
    print(url)
    user_agent_list = [
        "Mozilla/4.0(compatible; MSIE 6.0; Windows NT 5.ce1; SV1; AcooBrowser; .NET CLR ce1.ce1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0(compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0(compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.ce1; .NET CLR ce1.ce1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    ]
    user_agent = random.choice(user_agent_list)
    print('user_agent:{0}'.format(user_agent))
    headers = {
        "User_Agent": user_agent
    }
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    html = response.read().decode('utf-8')

    path = 'D:\\Pycharm\\rccode\\spider\\A05-\\B01\\baiduspider_html\\'
    with open(path + name + '吧第' + str(i)+'页html', 'w', encoding='utf-8') as f:
        f.write(html)


