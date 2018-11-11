'''
验证代理是否可用
'''
from urllib import request
from sys import exit
proxy_1 = request.ProxyHandler({"http": "180.104.63.125:9000"})

proxy_2 = request.ProxyHandler()

opener_1 = request.build_opener(proxy_1)
opener_2 = request.build_opener(proxy_2)

isProxy = input("please input y/n:")

if isProxy == "y":
    opener = opener_1
elif isProxy == "n":
    opener = opener_2
else:
    exit()

url = "https://www.baidu.com/"

req = request.Request(url)
response = opener.open(req)
print(response)