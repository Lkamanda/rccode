# from urllib import request
# url = "http://baidu.com"
# resp = request.urlopen(url)
# print(resp)
# print(type(resp))
# content = resp.read().decode('utf-8')
# print(content)

'''
w3c资料爬取
url = http://www.w3school.com.cn/json/index.asp
'''
from urllib import request
response = request.urlopen("http://www.w3school.com.cn/json/index.asp")
content = response.read().decode('gb2312')
print(content)