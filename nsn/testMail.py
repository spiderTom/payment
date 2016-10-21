# -*- coding: utf-8 -*-


import smtplib
from email.mime.text import MIMEText
import email.mime.multipart
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders


def send_mail():
    mailto_list = ['xxxx','xxx']#收件人
    mail_host = "xxxxx"  # 设置服务器
    mail_user = "xxxx"  # 用户名
    mail_pass = "xxxxxx"  # 口令
    mail_postfix = "xxxx.xxx"  # 发件箱的后缀
    me = "hello" + "<" + mail_user + "@" + mail_postfix + ">"  # 这里的hello可以任意设置，收到信后，将按照设置显示
    content = 'This is test mail!'#邮件正文
    msg = MIMEMultipart()
    body = MIMEText(content, _subtype='html', _charset='gb2312')  # 创建一个实例，这里设置为html格式邮件
    msg.attach(body)
    msg['Subject'] = "Subject Test"  # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(mailto_list)
    #附件内容，若有多个附件，就添加多个part, 如part1，part2，part3
    part = MIMEBase('application', 'octet-stream')
    # 读入文件内容并格式化，此处文件为当前目录下，也可指定目录 例如：open(r'/tmp/123.txt','rb')
    part.set_payload(open('test.txt','rb').read())
    Encoders.encode_base64(part)
    ## 设置附件头
    part.add_header('Content-Disposition', 'attachment; filename="test.txt"')
    msg.attach(part)

    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  # 连接smtp服务器
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(me, mailto_list, msg.as_string())  # 发送邮件
        s.close()
        print 'send mail sucess'
        return True
    except Exception, e:
        print str(e)
        return False