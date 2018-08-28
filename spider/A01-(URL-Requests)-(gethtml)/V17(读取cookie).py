from urllib import request
from http import cookiejar
filename = r'/home/tlxy/PCM/rccode/spliderexe/htmlcf/Cookie.txt'

cookie = cookiejar.MozillaCookieJar()

cookie.load(filename, ignore_discard=True, ignore_expires=True )
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(cookie_handler,http_handler,https_handler)

def getHomePage():
    url ='http://www.renren.com/967559915'
    rsp = opener.open(url)
    html = rsp.read().decode()
    html_path = r'/home/tlxy/PCM/rccode/spliderexe/htmlcf/'
    with open(html_path+'读取cookie获取html**V17'+'.html','w') as f:
        f.write(html)

if __name__ == '__main__':

    getHomePage()

