from urllib import parse,request
import ssl
from http import cookiejar
ssl._create_default_https_context = ssl._create_unverified_context
cookie_path = r'/home/tlxy/python/rccode/spliderexe/Cookies/V03Cookie.txt'
cookie = cookiejar.MozillaCookieJar(cookie_path)

cookie_handler =request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPHandler()

opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    url = 'https://security.kaixin001.com/login/login_post.php'

    data = {
        'email':'13231533164',
        'password':'5211314zxy.'
    }
    data = parse.urlencode(data)

    headers = {
        'Content-Length':len(data),
        'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }

    req = request.Request(url =url, data=data.encode(), headers=headers)
    rsq = opener.open(req)
    cookie.save(cookie_path,ignore_discard=True, ignore_expires=True)
if __name__ == '__main__':
    login()
