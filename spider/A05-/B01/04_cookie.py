'''
使用ccokie登陆
https://www.huawei.com/en/?ic_medium=direct&ic_source=surlent
method = post
登陆接口：https://www.huawei.com/en/accounts/LoginPost

'''

from urllib import request, parse
from http import cookiejar
# urllib 默认是get方法,如果想使用post方法,必须传入一个data 参数

# 生成cookie对象
filename = r"D:\Pycharm\rccode\spider\A05-\B01\baiduspider_html\cookie"
cookie = cookiejar.MozillaCookieJar(filename)
# cookie = cookiejar.CookieJar()
# 生成cookie 管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 生成http 请求管理器
http_handler = request.HTTPSHandler()
# 生成https 请求管理器
https_handler = request.HTTPHandler()

# 构建请求管理器
opener = request.build_opener(cookie_handler, http_handler, https_handler)

# 构建登录函数
def login(url):
    data = {
        "userName": "18612463553@163.com",
        "pwd": "785521zxy.",
        "language": "en",
        "fromsite": "www.huawei.com",
        "authMethod": "password"
    }
    data = parse.urlencode(data)
    print(type(data))

    # data 数据类型为bytes
    req = request.Request(url, data=bytes(data, "utf-8"))
    content = opener.open(req)
    content = content.read().decode("utf-8")
    print(content)
    cookie.save(ignore_discard=True, ignore_expires=True)
if __name__ == '__main__':
    url = "https://www.huawei.com/en/accounts/LoginPost"
    login(url)