'''
URLError的使用
'''
from urllib import request , error

if __name__ == '__main__':

    url = 'https://www.baiiiiiiiiiiiiiiduq.com/'
    # url = 'https://www.baidu.com/'
    try:

        req = request.Request(url)

        rsp = request.urlopen(req)

        # 读取完,后进行解码 的到html
        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
    #    print('URLError:{0}'.format(e.reason))
        print('URLError:{0}'.format(e))

    # except Exception as e:
    #     print(e)
    #
