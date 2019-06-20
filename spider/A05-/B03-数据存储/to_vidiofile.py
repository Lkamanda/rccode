# 音频文件的存储
# open('filename', 'wb') as f:
#    f.write()
'''
ce1.获取到下载文件的url 的地址，以二进制的格式下载
2.urllib
request.urlretrieve()
这个模块可以进行音频文件的下载
支持远程数据下载到本地
3.参数
url :下载资源的url地址
filename: 数据存储路径 + 文件名
reporthook: 要求回调函数,连接服务器时或下载完毕时触发该回调函数,显示当前的下载进度
data; 返回一个元祖，里面有俩个参数(filename,headers) ，参数引
4 request.urlretrieve(url, filename=None, reporthook=None, data=None)
'''
from urllib import request
import requests
import os
from lxml import etree
def Schedule(blocknum,blocksize,totalsize):
    '''
    显示下载进度
    :param blocknum:已经下载的数据块
    :param blocksize:数据模块大小
    :param totalsize:远程文件大小
    :return:
    '''
    per = 100.0*blocknum*blocksize/totalsize
    if per > 100:
        per = 100
    print("当前下载进度:{}".format(per))

user_agent = "Mozilla/4.0(compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)"
headers = {
    "User-Agent": user_agent
}
url = 'http://www.ivsky.com/'
response = requests.get(url=url, headers=headers)
html = etree.HTML(response.text)
img_url_list = html.xpath('//div[@class="syl_pic"]//img/@src')
for img_url in img_url_list:
    root_dir = 'img'
    # 判断是否存在路径，如果没有则，创建
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    filename = img_url.split('/')[-1]
    request.urlretrieve(url=img_url, filename=root_dir+"/"+filename, reporthook=Schedule)

# request.urlretrieve(url, filename='p1.jpg', reporthook='')
