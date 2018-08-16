'''
任务要求同V5只是使用Request 实现
'''
# header 身份切片 更改身份
import json
from urllib import request, parse

baseurl = 'http://fanyi.baidu.com/sug'

wd = input('input your keyword:')
data = {
    'kw': wd
}

data = parse.urlencode(data).encode('utf-8')
print(type(data))
# 使用request 通过header 模拟浏览器
headers = {
    'Content-Length': len(data)
}
# 构造一个Request类的实例
# Request 参数 url   data header (header为字典格式)
req = request.Request(url=baseurl, data=data, headers=headers)

# 因为我们已经构造了一个Request的请求实例,则所有的请求信息都可以封装在Requrst实例中
rsp =request.urlopen(req)
json_data= rsp.read().decode('utf-8')

# 把json字符串转换成字典
json_data = json.loads(json_data)
print(json_data)

for item in json_data['data']:
    print(item['k'],'--',item['v'])