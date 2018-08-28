import requests

import json
url = 'https://www.baidu.com/'
proxies={
    'http':'94.242.55.108:1448'
}

rsp = requests.request("get",url,proxies=proxies)

print(rsp.text)
print(rsp.json())