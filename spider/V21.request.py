import requests

url = 'http://www.baidu.com'
# 俩中请求方式
# -1 使用get请求
rsp = requests.get(url)
print(rsp.text)
filename = r'/home/tlxy/python/rccode/spliderexe/htmlcf/V21.html'
with open(filename,'w') as f:
    f.write(rsp.text)
# -2 使用request
rsp =requests.request("get",url)
print(rsp.text)

# 俩中请求的到结果相同