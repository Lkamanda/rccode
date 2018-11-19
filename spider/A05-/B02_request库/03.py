import requests
url = "https://www.12306.cn/mormhweb"
url1 = "https://kyfw.12306.cn/otn/resources/login.html"
response = requests.get(url1, verify=True)
response = requests.get(url1)
print(response.text)