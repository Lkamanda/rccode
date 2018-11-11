'''
使用FileCookieJar保存文件
'''
from urllib import request ,parse
from http import cookiejar
filename = r'/home/tlxy/PCM/rccode/spliderexe/htmlcf/Cookie.txt'


cookie = cookiejar.MozillaCookieJar(filename)
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():

    url = 'http://www.renren.com/PLogin.do'

    data = {
        'email': '18612463553',
        'password': '123456zxy'
    }

    data = parse.urlencode(data)
    req = request.Request(url, data=data.encode())
    rsp = opener.open(req)

    #保存cookie到文件
    #ignor_discard表示即使cookie将要被丢弃也要保存下来
    #ignore_expire 表示文件中cookie即时已经过期,保存
    cookie.save(ignore_discard=True, ignore_expires=True)

if __name__ == '__main__':
    login()

