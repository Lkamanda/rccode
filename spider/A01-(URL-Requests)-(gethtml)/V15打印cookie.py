from urllib import request,parse
from http import cookiejar

cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(cookie_handler,http_handler, https_handler)

def login():
    url = 'http://www.renren.com/PLogin.do'

    data = {
        'email':'18613463553',
        'password':'123456zxy'
    }

    data = parse.urlencode(data)
    req = request.Request(url, data=data.encode())
    rsq = opener.open(req)

if __name__ == '__main__':
    '''
    执行完login之后,会得到授权之后的cookie
    我们尝试把cookie打印出来
    '''
    login()
    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)



