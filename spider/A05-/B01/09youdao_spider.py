from urllib import request, parse
import json
import time
import hashlib
import random
def getMd5(value):
    # 构建md5对象
    md5 = hashlib.md5()
    md5.update(bytes(value, encoding="utf-8"))
    sign = md5.hexdigest()
    return sign
def yd_spidler(context):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    salt = int(time.time()*1000) + random.randint(0, 10)
    print(salt)
    print(type(salt))

    # sign =  n.md5("fanyideskweb" + e + t + "sr_3(QOHT)L2dx#uuGR@r")
    sign = "fanyideskweb" + context + str(salt) + "sr_3(QOHT)L2dx#uuGR@r "
    data = {
        "i": context,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": getMd5(sign),
        "doctype": "json",
        "version": "2.1"
    }

    data = parse.urlencode(data)
    print(len(data))
    user_agent_list = [
        "Mozilla/4.0(compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    ]
    user_agent = random.choice(user_agent_list)
    headers = {
        "User_Agent": user_agent,
        "Content_Length": len(data),
        "Accept-Language": "zh,en;q=0.9,en-US;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": " OUTFOX_SEARCH_USER_ID=-464647137@10.168.8.61; OUTFOX_SEARCH_USER_ID_NCOO=501927747.6189342; _ntes_nnid=c92a02814b68947a59e99a7062a9cc0e,1539100931992; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcg8WhlddglQ-CwKWkCw; ___rl__test__cookies=1542123305603"
    }

    req = request.Request(url=url, data=bytes(data, encoding="utf-8"), headers=headers)
    response = request.urlopen(req)
    html = response.read().decode()
    # json_data = json.loads(html)
    # for item in json_data["data"] :
    #     print(item['k'], item['v'])
    print(html)
if __name__ == '__main__':
    context = input("请输入翻译的词组:")
    yd_spidler(context)