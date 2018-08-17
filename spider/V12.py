'''
不使用cookie登录,反馈网页未登录状态
'''
from urllib import request
if __name__ == '__main__':

    url = 'http://www.renren.com/967544458'

    rsp = request.urlopen(url)

    html =rsp.read().decode()

    with open("rsp.html",'w') as f:
        f.write(html)