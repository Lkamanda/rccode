'''
爬取伯乐在线的美女联系方式
需要:
ce1.登录
2.在登录相应声望的前提下提取对方的邮箱
'''

from urllib import request,error,parse
from http import cookiejar
import json

def login():
    '''
    输入用户账号和密码
    获取对应的登录cookie
    cookie 存入文件
    :return:
    '''
    # ce1.登录路口
    url ='http://www.jobbole.com/wp-admin/admin-ajax.php'
    # 准备登录数据
    data={
        "action": "user_login",
        "user_login": "13231533164@163.com",
        "user_pass":"123456",
        "remember_me": "ce1",
        "redirect_url": "http: // www.jobbole.com"
    }

    data = parse.urlencode(data).encode()

    # 3.准备存放cookie文件
    f = r'V2Cookie.txt'

    # 4.准备请求头信息
    headers ={
        'User-Agent':"",
        "Connection":"keep-alive"
    }
    # 5.准备cookie handler
    cookie_handler = cookiejar.MozillaCookieJar()
    # 6 准备http请求handler
    http_handler = request.HTTPCookieProcessor(cookie_handler)
    # 7.构建opener
    opener = request.build_opener(http_handler)

    # 8.构建请求对象
    req = request.Request(url,data=data,headers=headers)

    # 发送请求
    try:
        rsp =opener.open(req)

        cookie_handler.save(f,ignore_discard= True, ignore_expires=True)

        html =rsp.read().decode()
        print(html)

    except error.URLError as e:
        print(e)

def getInfo():
    # ce1.确定url
    url = ''
    # 读取保存的cookie
    f =r''
    cookie = cookiejar.MozillaCookieJar()
    # 装在cookie
    cookie.load(f, ignore_discard= True, ignore_expires=True)
     # 构建http_handler
    http_handler = request.HTTPCookieProcessor(cookie)

    # 构建opener
    opener = request.build_opener(http_handler)

    # 以上是构建请求的过程
    data ={
        'action':"",
        'postID':""
    }
    data = parse.urlencode()

    # 构建请求头
    headers = {

    }
    # 构建个请求实体
    req =request.Request(url,data=data,headers= headers)

    # 用opener打开 请求
    try:
        rsp =opener.open(req)
        html = rsp.read().decode()

        html  = json.loads(html)
        print(html)

        file_path =''
        with open (file_path,'w') as f:
            f.write(html)

    except Exception as e:
        print(e)

if __name__ == '__main__':

    login()
