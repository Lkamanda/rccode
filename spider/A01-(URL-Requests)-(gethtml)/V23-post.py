
import requests
import json
url = 'http://fanyi.baidu.com/sug'
data = {
    'kw':'boy'
}



headers = {
    'Content-Length':str(len(data))
}

rsp =requests.post(url=url, data=data, headers=headers)


print(rsp.json())

