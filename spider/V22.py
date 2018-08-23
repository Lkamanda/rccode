'''
使用参数headers 和params
研究返回结果
'''
import requests
# 完整的url 是有下面url加上参数构成的
url = 'http://baidu.com/s?'

kw = {
    "wd":"王八蛋"
}

#  headers 来自与网页的Request Headers ,正常情况下应尽可能的全
headers = {
    "User-Agent":"Mozilla/5.0(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}

# 不需要向urllib那样编码  直接kw
rsp = requests.get(url, params= kw, headers= headers)
# text 需要解码
print(rsp.text)
print(rsp.content) #内容
# print(rsp.url)
# print(rsp.encoding)  编码格式
# print(rsp.status_code)  请求返回吗