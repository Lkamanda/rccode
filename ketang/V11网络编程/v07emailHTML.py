from email.mime.text import MIMEText
import smtplib
mail_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Title</title>
        </head>
        <h1> 这是一封HTML格式邮件</h1>
        </body>
        </html>
        """
msg = MIMEText(mail_content, "html", "utf-8")

# 构建发送者地址和登录信息
from_addr = "1599200510@qq.com"
from_pwd = "imfznupxaoiiihfe"
to_addr = "1599200510@qq.com"
smtp_srv = "smtp.qq.com"
try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)
