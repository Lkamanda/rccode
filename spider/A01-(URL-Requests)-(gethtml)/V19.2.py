# '''
# V2
# '''
# '''
# 通过查看js,能找到js代码中
# ce1. 这个是计算salt 的公式
# r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10)):
# 2:sign
# i = n.md5("fanyideskweb" + t + r + "ebSeFb%=XZ%T[KZ)c(sy!");
# md5 一共需要四个参数,第一个和第四个都是固定值的字符串,第三个是所谓的salt,第二个是参数就是输入的要查找的单词
# '''
import time , random
import hashlib
from urllib import request ,parse

# 得到salt
def getSalt():
    # salt 公式是: "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
    # 随机生成一个0到1的小数,乘10然后取整
    # 把他翻译成python代码

    salt = int((time.time()*1000)) + random.randint(0,10)
    return salt

# MD5 的python实现
def getMD5(v):
    # sign公式 : n.md5("fanyideskweb" + t + r + "ebSeFb%=XZ%T[KZ)c(sy!")
    # 生成一个md5 实例
    md5 = hashlib.md5()
    # md5使用upadate 计算

    # update 需要一个bytes格式的参数
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()
    return sign

# 得到可以使用的sign
def getSign(key,salt):

    sign = 'fanyideskweb' + key +str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"
    sign = getMD5(sign)

    return sign

def yd(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    salt = getSalt()
    data ={
        "i": key,
        "from":"AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        # 加密
        "client": "fanyideskweb",
        #  加盐
        "salt": str(salt),
        "sign": getSign(key,salt),
        "doctype": "json",
        "version": "2.ce1",
        "keyfrom": "fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult": "false"
    }
    print(data)
    data = parse.urlencode(data).encode()
    headers = {
        "Accept":"application/json, text/javascript, */*;q=0.01",
        #"Accept-Encoding":"gzip,deflate",
        "Accept-Language":"zh-CN,zh;q = 0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
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
    yd("girl")