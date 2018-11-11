from urllib import request
import random
proxy_list = [
    {"HTTP": "211.147.239.101:41062"},
    {"HTTP": "180.118.128.50:9000"},
    {"HTTP": "121.232.148.170:9000"}
]
proxy = random.choice(proxy_list)
print("使用的代理是:{0}".format(proxy))
# 构建代理管理器
proxy_handler = request.ProxyHandler(proxy)
# 创建网络请求对象opener
opener = request.build_opener(proxy_handler)
url = "http://baidu.com"
headers = {
"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
req = request.Request(url, headers=headers)
response = opener.open(req)
html = response.read().decode()
print(html)