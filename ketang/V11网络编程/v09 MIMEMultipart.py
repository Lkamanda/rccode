# 构建附件使用
from email.mime.text import MIMEText
# 构建基础邮件使用
from email.mime.multipart import MIMEBase, MIMEMultipart
mail_mul = MIMEMultipart()
# 构建邮件正文
mail_text = MIMEText("Hello i am xiao lin", "plain", "utf-8")
# 把构建好的正文邮件附加入邮件中
mail_mul.attach(mail_text)

# 构建附件
# 构建附件,需要从本地读入附件
# 打开一个本地文件
# 以rb 格式打开
with open("02.html", "rb") as f:
    s = f.read()
    # 设置附件的MIME和文件名
    m = MIMEText(s, 'base64', "utf-8")
    m["Content-Type"] = "application/octet-stream"
    # 需要注意
    # 1. attachment 后分为英文状态
    # 2. filename 后面需要用引号包裹,注意与外面的一号错开
    m["Content-Disposition"] = "attachment:filename='02.html'"
    # 添加到MIMEMultipart
    mail_mul.attach(m)
from_addr = "1599200510@qq.com"
from_pwd = "imfznupxaoiiihfe"
to_addr = "1599200510@qq.com"
smtp_srv = "smtp.qq.com"
try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    srv.sendmail(from_addr, [to_addr],mail_mul.as_string())
    srv.quit()
except Exception as e:
    print(e)
