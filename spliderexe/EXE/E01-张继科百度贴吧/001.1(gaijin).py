'''
在01基础上加入代理,写入
'''
from urllib import request,error,parse


# def saveHtml(file_name,file_content):
#     # file_name 文件名
#     # file_content 写入内容
#     with open(file_name.replace('/','_')+".html","wb") as f:
#         f.write(file_content)


if __name__ == '__main__':
    #使用代理
    # ce1.设置代理
    property = {'http':'140.250.222.3:80'}
    # 2.创建property_handle
    property_handle = request.ProxyHandler(property)
    # 3.创建opener
    opener = request.build_opener(property_handle)
    # 4.安装opener
    request.install_opener(opener)

    qs ={
        'kw':'张继科',
        'ie':'utf-8',
        'pn': 0
    }


    baseurl = 'https://tieba.baidu.com/f?'
    # 假定只取10页
    for i in range(10):
        pn = i*50
        qs['pn'] = str(pn)
        url = baseurl + parse.urlencode(qs)
        print(type(url))

        rsp = request.urlopen(url)

        html = rsp.read()
        print(type(html))

            # 写入html文件
            # 待修改文件名称
            # 把文件放到指定路径下
        a = '张继科贴吧第{0}'.format(i) + '页'
        with open(a + ".html", "wb") as f:
            f.write(html)


