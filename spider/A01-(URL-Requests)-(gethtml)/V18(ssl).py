'''
对没有经过的ssl协议的进行处理
'''
from urllib import request
# 导入python ssl 处理模块

import ssl
# 利用证书上下文环境替换认证的向下问环境
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.12306.cn/mormhweb/"

rsp = request.urlopen(url)
html =rsp.read().decode()
print(html)





