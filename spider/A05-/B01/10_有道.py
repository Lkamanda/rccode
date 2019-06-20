from urllib import request, parse
import hashlib
import time
import random
import json

def youdou_spider(content):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    user_agent_list = [
        "Mozilla/4.0(compatible; MSIE 6.0; Windows NT 5.ce1; SV1; AcooBrowser; .NET CLR ce1.ce1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0(compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0(compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.ce1; .NET CLR ce1.ce1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    ]
    user_agent = random.choice(user_agent_list)

    salt = int(time.time()*1000 + random.randint(0, 10))
    #  n.md5("fanyideskweb" + e + t + "sr_3(QOHT)L2dx#uuGR@r")
    sign = "fanyideskweb" + content + str(salt) + "sr_3(QOHT)L2dx#uuGR@r"
    data = {
        "i": content,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": getMd5(sign),
        "doctype": "json",
        "version": "2.ce1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    data = parse.urlencode(data)
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh,en;q=0.9,en-US;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-464647137@10.168.8.61; OUTFOX_SEARCH_USER_ID_NCOO=501927747.6189342; _ntes_nnid=c92a02814b68947a59e99a7062a9cc0e,1539100931992; JSESSIONID=aaazIZwTu8sKX-PfINBCw; ___rl__test__cookies=1542356731318",
        "Host": "fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": user_agent,
        "X-Requested-With": "XMLHttpRequest"
    }
    req = request.Request(url=url, data=bytes(data, encoding="utf-8"), headers=headers)
    response = request.urlopen(req)
    html = response.read().decode()
    # print(html)
    yd_parse(html)

# md5 加密
def getMd5(value):
    md5 = hashlib.md5()
    md5.update(bytes(value, encoding="utf-8"))
    sign = md5.hexdigest()
    return sign
# 加密数据
def yd_parse(html):
    data_json = json.loads(html)
    sr_dict = data_json['smartResult']
    items = sr_dict["entries"]
    # print(items)
    for i in items:
        print(i)
if __name__ == '__main__':
    while True:
        content = input("请输入你想翻译的字符:")
        if content =="q":
            break
        else:
            youdou_spider(content)