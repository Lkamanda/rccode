from urllib import request
from http import cookiejar
cookie_path ='/home/tlxy/python/rccode/spliderexe/Cookies/V03Cookie.txt'

cookie =cookiejar.MozillaCookieJar()
cookie.load(cookie_path, ignore_discard=True, ignore_expires=True)

cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler, https_handler, cookie_handler)

def getZhuYe():
    url ='http://www.kaixin001.com/friend/search.php'
    # url = 'http://www.kaixin001.com/app/recent.php?r=0.349971838211949'

    rsp = opener.open(url)

    html = rsp.read().decode()

    html_path = r'/home/tlxy/python/rccode/spliderexe/htmlcf/E03-zhuye.html'

    with open(html_path,'w') as f:
        f.write(html)
if __name__ == '__main__':
    getZhuYe()
