from tkinter import *
import requests
from urllib import request
import random
from bs4 import BeautifulSoup


'''
# 163 歌曲外链 http://music.163.com/song/media/outer/url?id={}.mp3.format(id)
# 获取页面源码 : https://music.163.com/#/playlist?id=2521554648
# 获取歌曲id ,以及歌曲名称
# 下载歌曲

#href="/song?id=1345299173"
'''


def getUser_Agent():
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 '
        '(KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 '
        '(KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .N'
        'ET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) '
        'Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; '
        '.NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) '
        'QQBrowser/6.9.11079.201'
    ]
    user_agent = random.choice(user_agent_list)
    return user_agent


def get_headers():
    User_Agent = getUser_Agent()
    headers = {
        "Host": "music.163.com",
        "User-Agent": User_Agent,
        "Referer": "https://music.163.com/"
    }
    return headers


def music_spider():
    # 获取用户输入的url地址
    # url = entry.get()
    url = 'https://music.163.com/#/playlist?id=2521554648'
    headers = get_headers()
    res = requests.get(url=url, headers=headers)
    html = res.text
    print(html)
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('span', {'class': 'txt'})
    print(items)
    for item in items:
        href = item.find_all('a')[0].get('href')
        print(href)
    # 拼接url地址
    # 设置下路径
    # 下载



def views():
    # 创建窗口
    root = Tk()
    # 设置窗口标题
    root.title('网易云音乐下载')
    # 设置窗口大小
    root.geometry("850x500")
    # 设置窗口出现在屏幕中的位置
    root.geometry("+100+100")

    # 第o行
    # 设置下载器标签
    label = Label(root, text='请输入你的下载地址:', font=('华文行楷', 20))
    # 定位
    label.grid()
    # 设置输入框
    entry = Entry(root, font=('微软雅黑', 20), width=30)

    entry.grid(row=0, column=1)

    # 第一行
    # 设置列表框
    text = Listbox(root, font=('隶书', 20), width=50, height=15)
    text.grid(row=1, columnspan=2)
    # 设置按钮  开始
    button1 = Button(root, text='Start', font=('微软雅黑', 25), command=music_spider())
    button1.grid(row=2, column=0, sticky='s')    # sticky 对齐方式 N S W E

    # 设置按钮 结束
    button2 = Button(root, text='End', font=('微软雅黑', 25), command=root.quit)
    button2.grid(row=2, column=1, sticky='s')
    # 显示窗口,显示消息回环
    # 将数据添加到控件中
    # text.insert(END, '下载')
    # # 文本自动向下滚动
    # text.see(END)
    # # 更新
    # text.update()
    root.mainloop()





# 主函数
def wy_main():
    views()


if __name__ == '__main__':
    wy_main()