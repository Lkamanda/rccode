'''
利用parse模块模拟post请求
分析百度翻译
分析步骤
ce1. f12
2. 尝试输入girl,发现每敲一个单词都有请求
3.请求地址:http://fanyi.baidu.com/sug
4.利用NetWork-Hearders 查看,发现 FormData的值是 kw:girl
5.检查返回内容格式,发现返回的是json格式内容


流程:
模拟一个url,url里包含我们的form数据
发送,发送后会给我们一个反馈,这个反馈是jsonge格式的这个时候我们将它读出来
'''

from urllib import request,parse

# 负责处理joson数据模块
import json

'''
大致流程:
ce1.利用data结构内容,然后urlopen打开
2.返回一个json格式的结果
3.返回结果就应该是girl的释义
'''

baseurl = 'http://fanyi.baidu.com/sug'

# 用来存放模拟form的数据一定是dict格式
wd = input('input your keyword:')

data= {
    # girl 是翻译输入的英文内容,应该是有用户输入,此处使用硬编码
    'kw': wd
}

# 需要使用parse模块对data进行编码

# data = parse.urlencode(data)得到的数据类型是str
# 这是我们需要使用encode() 转换其数据类型 ,可以指定,也可让其默认
data = parse.urlencode(data).encode('utf-8')
print(type(data))
# 需要构造有一个请求头,请求头至少包含传入的数据长度
# request要求传入的请求头是一个dict格式

headers = {
    # 因为使用post,至少应该包含content-length 字段
    'Content-Length':len(data)
}

# 有了headers ,data ,url,就可以尝试发出请求了

rsp = request.urlopen(baseurl, data = data )

json_data = rsp.read().decode('utf-8')
print(type(json_data))
print(json_data)

# 把json字符串类型转换成字典
# json.load()
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'],'--', item['v'])