from urllib import request,parse
'''
掌握对url进行参数编码的方法
需要使用parse模块
'''
if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'

    wd = input('input your keyword:')

    # 要想使用data需要字典结构
    qs = {
        "wd":wd
    }
    print(qs)
    # 转换url编码
    qs = parse.urlencode(qs)
    print('###')
    print(qs)

    fullurl = url + qs
    print(fullurl)

    # 如果直接用可读带参数的url,是不能访问的
    rsp = request.urlopen(fullurl)



    # print(type(rsp))
    # print(rsp)
    #
    # print('url: {0}'.format(rsp.geturl()))
    # print('Info: {0}'.format(rsp.info()))
    # print('Code: {0}'.format(rsp.getcode()))

    html = rsp.read()

    html = html.decode()

    print(html)