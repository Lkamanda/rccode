from urllib import request
import chardet

if __name__ == '__main__':


    url = 'http://news.baidu.com/'

    rsp = request.urlopen(url)
    print(type(rsp))
    print(rsp)

    print('url: {0}'.format(rsp.geturl()))
    print('info: {0}'.format(rsp.info()))
    print('code: {0}'.format(rsp.getcode()))

    html = rsp.read()

    cs = chardet.detect(html)

    html = html.decode(cs.get('encoding','utf-8'))

