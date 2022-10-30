# -*- coding: utf8 -*-
import requests
import smtplib
import datetime
import json
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

sender_mail = 'mahoo12138@qq.com' #这里填发件人邮箱
sender_pass = '*************' #这里填SMTP授权码
to='mahoo12138@outlook.com'  #这里填收件人邮箱

def sendEmail(sender_mail,sender_pass,to):
    url='https://v1.hitokoto.cn?c=h&c=d&h=j'
    res=requests.get(url).json()
    hito_msg='\n' + res['hitokoto'] + '   ' + '—— ' + res['from']
    print(hito_msg)
    timeinfo = '现在是北京时间：' + str(datetime.datetime.now().strftime('%Y-%m-%d')) + ' 23:30:00\n\n已经很晚了，该睡觉啦！\n'
    msg = timeinfo + hito_msg
    # 设置总的邮件体对象，对象类型为mixed
    msg_root = MIMEMultipart('mixed')
    # 邮件添加的头尾信息等
    msg_root['From'] = '黄昌河<Mahoo12138>' #发送人描述
    msg_root['To'] = to
    # 邮件的主题，显示在接收邮件的预览页面
    subject = '晚安，该睡觉啦！'  #邮件标题
    msg_root['subject'] = Header(subject, 'utf-8')

    # 构造文本内容
    text_info = msg

    text_sub = MIMEText(text_info, 'plain', 'utf-8')
    msg_root.attach(text_sub)

    try:
        sftp_obj =smtplib.SMTP('smtp.qq.com', 25)
        sftp_obj.login(sender_mail, sender_pass)
        sftp_obj.sendmail(sender_mail, to, msg_root.as_string())
        sftp_obj.quit()
        print('Send Email successful!')
        

    except Exception as e:
        print('Send Email failed next is the reason')
        print(e)

    


def main_handler(event, context):
    sendEmail(sender_mail,sender_pass,to)
    return("{To:" + to + ", 执行结果: 1}")


if __name__ == '__main__':
    main_handler("", "")