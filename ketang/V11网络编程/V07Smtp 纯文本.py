import smtplib
from email.mime.text import MIMEText

# MIMEText 三个主要参数
# ce1.邮件内容
# 2.MIME 子类型,在此案例我们使用plain 表示text
# 3,邮件编码格式
msg = MIMEText("Hello ia xiaolin ", "plain", "utf-8")
# 发送email地址,此处地址直接使用我的qq邮箱,密码一般需要临沭输入
from_addr = "1599200510@qq.com"
from_pwd = "imfznupxaoiiihfe"
# 收件人信息
to_addr = ["819143024@qq.com", "1599200510@qq.com", "1500977956@qq.com"]


# 输入SMTP 服务器地址
# 此处根据不同的邮件服务商不同设置不同的值,
# 现在基本任何一家邮件服务商,如果采用第三方邮件,都需要开启授权选线
# 腾讯qq邮箱的stmp 地址是smtp.qq.com
smtp_srv = "smtp.qq.com"

try:
    # 第一个参数
    # SMTP协议默认端口25
    # 需要对SMTP地址进行编码,一定是bytes格式
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    # SMTP协议默认端口号465
    # 登录邮箱发送
    srv.login(from_addr, from_pwd)
    # 发送邮件
    # 三个参数
    # ce1.发送地址
    # 2.接受地址,必须是list形式
    # 3. 发送内容,作为字符串发送
    srv.sendmail(from_addr, to_addr, msg.as_string())
    srv.quit()
except Exception as e:
    print(e)
