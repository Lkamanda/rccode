'''
访问一个网址
使用add_header伪装
'''

from urllib import request,error

if __name__ =='__main__':

    url = 'https://baidu.com'

    try:

        #使用add_header 伪装访问
        req = request.Request(url)
        # add_header (self, key, value)
        req.add_header('User-Agent','User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')

        # 正常访问
        rsp = request.urlopen(req)
        html =rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)

    except error.URLError as e:
        print(e)

    except error as e:
        print(e)

    print('Done->>>')
