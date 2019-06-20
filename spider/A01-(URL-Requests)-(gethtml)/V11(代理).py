'''
代理的基本使用
使用代理访问百度网站
'''

from urllib import request,error
if __name__ == '__main__':

    url = 'https://www.baidu.com/'

    # 使用代理
    # -ce1 设置代理
    proxy = {'http': '140.205.222.3:80'}

    # -2 创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)

    # -3 创建opener
    opener = request.build_opener(proxy_handler)

    # -4 安装Opener
    request.install_opener(opener)

    # 现在就可以访问url,则使用的是代理服务器
    try:

        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

