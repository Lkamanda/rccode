'''
使用urllib.reques请求一个网页内容,并把内容打印出来
'''
from urllib import request
if __name__ =='__main__':
    url = 'https://jobs.zhaopin.com/CZ294133230J00050390411.htm'
    # 打开相应的url并把相应页面做为返回
    rsp=request.urlopen(url)

    #把返回的结果打印出来
    #读取出来的内容为bytes
    html = rsp.read()

    print(type(html))

    # 如果想把bytes解码需要
    html = html.decode('utf-8')
    print(html)
