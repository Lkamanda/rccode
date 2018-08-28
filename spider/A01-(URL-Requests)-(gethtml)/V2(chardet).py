'''
利用request下载页面
自动检测页面编码
'''


from urllib import request
import chardet
if __name__ == '__main__':
    url = 'https://news.china.com/focus/jggjxdd/13000773/20180813/33552593.html?xw002'

    rsp = request.urlopen(url)

    html = rsp.read()

    # 解码
    # 利用 chardet 自动检测

    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # 使用get的好处 取值保证不会出错
    html = html.decode(cs.get('encoding', 'utf-8'))
    print(html)

