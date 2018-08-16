'''
爬去百度贴吧,张继科把
1.张继科吧 url = https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=0
2.进去贴吧很多页

    第二页网址: https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=50
    第三页网址: https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=100
    第四页网址: https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=150
    第五页网址: https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=200
    第六页网址: https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=250

3.由上面网站可以找到一些规律,每一页只有后面数字不同,且数字应该是(页数-1)×50

解决办法:
1.准被构建参数字典
    -字典包扣三部分 kw ,ie ,pn(pagenumber)
2. 使用parse构建完整url
3. 使用for 循环写入下载

'''
from urllib import request,parse
if __name__ == '__main__':

    # 1. 准备构建字典
    qs = {
        'kw': '张继科',
        'ie': 'utf-8',
        'pn': 0
    }

    # 2.使用parse构建完整url
    # 我们假定只需要前10页
    urls = []
    baseurl = "https://tieba.baidu.com//f?"
    for i in range(10):
        pn = i *50
        qs['pn'] = str(pn)

        # 把qs编码后的url和基础url进行拼接
        # 拼接完毕后放入urls列表中
        urls.append(baseurl + parse.urlencode(qs))
    print(urls)
    # 3.使用for循环写入下载

    for url in urls:

        rsp = request.urlopen(url)

        html = rsp.read().decode('utf-8')
        print(url)
        print(html)

'''
待完善
1.把每个抓到的内容保存到文件中,后缀为html
'''