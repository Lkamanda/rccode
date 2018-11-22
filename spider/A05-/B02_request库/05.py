import requests
import os
url = "https://i.meizitu.net/2018/11/13c08.jpg"
headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "Referer": "https://www.mzitu.com/"
}
req = requests.get(url=url, headers=headers)
path = 'meizi'
if not os.path.exists(path):
    os.makedirs(path)
with open(path + "\\x" + ".jpg", "wb") as f:
    f.write(req.content)
    f.close()
# url = "https://i.meizitu.net/2018/11/13c01.jpg"
# html = requests.get(url)
# with open('picture.jpg', 'wb') as file:
#     file.write(html.content)