'''
构建代理集群/列队
每次访问服务器,随机抽取一个代理
抽取可以使用random.choice

分析步骤:
1.构建代理群
2.每次访问,随机选取代理并执行
'''
from urllib import request,error
import random
proxy_list = [
    # 列表中存放的是dict类型的元素
    {'http': '221.7.255.168:8080'},
    {'http': '122.72.18.60:80'},
    {'http': '113.200.56.13:8010'},
    {'http': '39.106.160.36:3128'},
    {'http': '60.195.198.245:3128'},
]

if __name__ == '__main__':
    a = input('输入:')

    url = 'https://www.baidu.com'
    for item in range(int(a)):
    # 使用代理集群
        proxy_handler_list =[]
        for proxy in proxy_list:
            proxy_handler = request.ProxyHandler(proxy)
            proxy_handler_list.append(proxy_handler)

        opener_list = []
        for proxy_handler in proxy_handler_list:
            opener =request.build_opener(proxy_handler)
            opener_list.append(opener)

        try:
            # 安装opener
            # 每次登录前从代理列表中随机抽取一个数据
            opener = random.choice(opener_list)
            request.install_opener(opener)
            rsp = request.urlopen(url)
            html = rsp.read().decode()
            print(opener)
            print(html)

        except error.HTTPError as e:
            print(e)
        except error.URLError as e :
            print(e)
        except Exception as e:
            print(e)
