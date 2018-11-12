'''
百度翻译功能的实现
'''

from urllib import request, parse
import random
import json
url = "https://fanyi.baidu.com/?aldtype=16047#auto/zh"
user_agent_list = [
"Mozilla/4.0(compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0(compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0(compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
]
user_agent = random.choice(user_agent_list)

# 使用的post 请求
def db_spider(content):
    # 构建data
    data = {
        "kw": content
    }
    # 参数的分装转码
    data = parse.urlencode(data)
    url = "https://fanyi.baidu.com/sug"
    # 封装headers头部信息
    headers ={
        'Content-Length': len(data),
        'User_Agent': user_agent
    }
    req = request.Request(url=url, data=bytes(data, encoding='utf-8'), headers=headers)
    response = request.urlopen(req)
    html = response.read().decode()

    # 格式化数据
    json_data = json.loads(html)
    for item in json_data['data'] :
        #print(item)
        print(item['k'], item['v'])


if __name__ == '__main__':
    content = input("请输入你想翻译的词组:")
    db_spider(content)