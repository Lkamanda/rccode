import requests
import os
src = "http://pic13.nipic.com/20110330/2883687_091610438124_2.jpg"
url = "http://img3.imgtn.bdimg.com/it/u=2200166214,500725521&fm=26&gp=0.jpg"
root = 'pictures'
path = root + "/" + src.split('/')[-1]
response = requests.get(url=src)
try:
    # 判断路径是否存在
    if not os.path.exists(path=root):
        # 如果路径不存在则创建路径
        os.mkdir(root)    # 创建路径
    if not os.path.exists(path):
        response = requests.get(url)
        # 写入图片需要使用流文件写入, 使用wb
        with open(path, 'wb') as f:
            f.write(response.content)
            print('文件保存完成')
    else:
        print('文件已经存在')
except:
    print("文件保存失败")