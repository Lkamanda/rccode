'''
爬取登录开心网
利用cookie
免除ssl
'''
'''
操作步骤
1.寻找入口,搜索相应文字可以快速定位
2. 构造opener
3.构造login函数
'''

#login_url="https://security.kaixin001.com/login/login_post.php"

from urllib import request,parse
from http import cookiejar
import ssl
# 忽略ssl安全问题
ssl._create_default_https_context = ssl._create_unverified_context

# 定义cookie存放路径
filename = r'/home/tlxy/python/rccode/spliderexe/Cookies/kaixin.com:Cookie.txt'

cookie = cookiejar.MozillaCookieJar(filename)
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPHandler()
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login ():
    login_url ='https://security.kaixin001.com/login/login_post.php'
    data = {
        "email":"13231533164",
        "password":"5211314zxy."
    }
    data = parse.urlencode(data)
    # http协议请求头
    headers = {
        "Content-length":len(data),
        # 伪装浏览器
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
    }
    # 对post 的data内容进行编码

    # 构建请求Request对象
    # data要求是一个bytes对象,所以需要进行编码
    req =request.Request(url= login_url, data=data.encode(), headers=headers)

    rsp = opener.open(req)

    # # 读取后解码
    html =rsp.read().decode()

    # 保存cookie
    # cookie.save(ignore_discard = True, ignore_expires =True)
    # print(html)
    html_path = r'/home/tlxy/python/rccode/spliderexe/htmlcf/kaixin.html'
    with open (html_path,'w') as f:
        f.write(html)

def getHomePage():
    base_url = 'http://www.kaixin001.com/home/?_profileuid=181777494&t=72'

    rsp  =opener.open(base_url)
    html_zhuye =rsp.read().decode()
    html_zhuye_path = r'/home/tlxy/python/rccode/spliderexe/htmlcf/kx_zhuye.html'

    with open(html_zhuye_path,'w') as f:
        f.write(html_zhuye)
    print(html_zhuye)
if __name__ == '__main__':
    login()
    getHomePage()

