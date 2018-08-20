'''
破解有道词典
'''

from urllib import request, parse

def youdao(key):

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    data = {
        # 从网页获取
        'i':'girl',
        'from':'AUTO',
        'to':'AUTO' ,
        'smartresult':'dict',
        'client': 'fanyideskweb',
        'salt': '1534756089015' ,
        'sign': '984d21a000e0d4be4c5cf260521f1090',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'False'
    }
    # 参数data需要的是data 格式
    data = parse.urlencode(data).encode()
    headers = {
                "Accept": "application/json,text/javascript,*/*; q = 0.01",
                #"Accept-Encoding": "gzip, deflate",
                "Accept-Language":" zh - CN, zh;q = 0.9",
                "Connection": "keep - alive",
                "Content-Length": "200",
                "Content-Type": "application/x-www-form-urlencoded;charset =UTF-8",
                "Cookie": "OUTFOX_SEARCH_USER_ID = 913703642 @ 10.168.8.64;JSESSIONID = aaahJVAJEDZY2a0UL9pvwOUTFOX_SEARCH_USER_ID_NCOO = 1511375463.4115808;___rl__test__cookies = 1534756089008",
                "Host":" fanyi.youdao.com",
                "Origin":"http://fanyi.youdao.com",
                "Referer":"http://fanyi.youdao.com/",
                "User-Agent":"Mozilla/5.0(X11;Linux x86_64) AppleWebKit/537.36(KHTML, likeGecko)Chrome/64.0.3282.119Safari/537.36",
                "X-Requested-With":" XMLHttpRequest"
    }
    req = request.Request(url=url, data =data, headers =headers)
    rsp = request.urlopen(req)
    html  =rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao("girl")

# https://fishc.com.cn/thread-106892-1-1.html