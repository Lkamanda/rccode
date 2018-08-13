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
headers = {
    'Conten-Length': len(data)
}

rsp =request.urlopen(baseurl, data=data)
json_data= rsp.read().decode('utf-8')

# 把json字符串转换成字典
json_data = json.loads(json_data)
print(json_data)

for item in json_data['data']:
    print(item['k'],'--',item['v'])