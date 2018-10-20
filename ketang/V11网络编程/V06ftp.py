import ftplib
import os
import socket

HOST = "ftp.acc.umu.se"
DIR = "Public/EFLIB/"
FILE = "README"

try:
    f = ftplib.FTP()
    # 通过设置调试级别可以方便调试
    f.set_debuglevel(2)
    # 链接主机地址
    f.connect(HOST)
except Exception as e:
    print(e)
    exit()
print("***Connected to host{0}".format(HOST))

try:
    # 登录如果没有输入用户信息,则默认使用匿名登录
    f.login()
except Exception as e:
    print(e)
    exit()

# 客户端和服务器进行各种文件传输和信息查询操作
try:
    # 更改当前目录到指定目录
    f.cwd(DIR)
except Exception as e:
    print(e)
    exit()
print("****Change dir to{0}".format(DIR))
try:
    # 从FTP 服务器上下载文件
    # 第一个参数是ftp命令
    # 第二个参数是回调函数
    # 此函:执行RETR命令, 下载问价到本地后,运行回调函数
    f.retrbinary('RETR{0}'.format(FILE), open(FILE, 'wb').write)
except Exception as e:
    print(e)
    exit()
# 4客户端从远程FTP服务器退出,结束传输
f.quit()



