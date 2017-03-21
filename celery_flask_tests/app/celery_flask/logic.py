#coding:utf-8
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header



def do_send_email(fromemail, toemail, subject, content):

    #server.login("1443556385@qq.com", "zmudpwcqciiujbdg")
    host_server = 'smtp.qq.com'
    # sender_qq为发件人的qq号码
    sender_qq = fromemail
    # pwd为qq邮箱的授权码
    pwd = 'zmudpwcqciiujbdg'
    # 发件人的邮箱
    sender_qq_mail = fromemail
    # 收件人邮箱
    receiver = toemail
    # 邮件的正文内容
    mail_content = content
    # 邮件标题
    mail_title = subject

    # ssl登录
    smtp = SMTP_SSL(host_server)
    smtp.login(sender_qq_mail, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()

