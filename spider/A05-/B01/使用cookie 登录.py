from urllib import request, parse
from http import cookiejar

filename = r"D:\Pycharm\rccode\spider\A05-\B01\baiduspider_html\cookie"
cookie = cookiejar.MozillaCookieJar(filename)
cookie_handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(cookie_handler)
url = "https://www.huawei.com/en/accounts/LoginPost"
req = request.Request(url)
content = opener.open(req)
html = content.read().decode("utf-8")
html_file = r"D:\Pycharm\rccode\spider\A05-\B01\huawei_login.html"
with open("html_file", "w") as f:
    f.write(html)
