import requests

response = requests.get("http://www.baidu.com")
# 返回cookie对象
cookiejar = response.cookies
# 将cookiejar转换成字典
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
print(cookiedict)