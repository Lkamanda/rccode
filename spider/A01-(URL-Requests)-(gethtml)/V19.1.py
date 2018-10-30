'''
v01 True
'''
from urllib import request,parse

def yd(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data ={
        "i": "boy",
        "from":"AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        # 加密
        "client": "fanyideskweb",
        #  加盐
        "salt": "1534814740723",
        "sign":"346b4c35320f93759adc912d4426e89f",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult": "false"
    }

    data = parse.urlencode(data).encode()
    headers = {
        "Accept":"application/json, text/javascript, */*;q=0.01",
        #"Accept-Encoding":"gzip,deflate",
        "Accept-Language":"zh-CN,zh;q = 0.9",
        "Connection":"keep-alive",
        "Content-Length": "199",
        "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID = 974491457@10.168.8.76;OUTFOX_SEARCH_USER_ID_NCOO=313284266.9521205;DICT_UGC = be3af0da19b5c5e6aa4e17bd8d90b28a|;JSESSIONID = abcGvK2pl - nnj4pRbfAvw;_ntes_nnid = bc9ba5b1e189eaaa53885a8bbe8564eb, 1534814616179;___rl__test__cookies = 1534814740706",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/?keyfrom=fanyi-new.logo",
        "User-Agent": "Mozilla/5.0(X11; Linuxx86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/64.0.3282.119Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':

    yd("boy")