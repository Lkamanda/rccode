import requests

url = "https://item.jd.com/35107229889.html?jd_pop=b543a3f3-3956-4114-879c-1580c9d72906&abt=0"
try:
    response = requests.get(url=url)
    print(response.text) # 响应字符串
    print(response.content)  # 响应得到字节流
    # 获取完整url地址
    print(response.url)
    print(response.encoding)
    # 查看原文的编码类型
    print(response.apparent_encoding)
    # 查看响应码
    print(response.status_code)
except:
    pass