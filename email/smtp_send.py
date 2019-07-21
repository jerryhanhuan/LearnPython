#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:smtp_send.py
#Created Time:2019-07-21 10:31:16


import smtplib
from email.mime.text import MIMEText



def main():
    msg = MIMEText('hello,send by python...','plain','utf-8')
    #输入 Email 地址和口令
    from_addr = input('From:')
    password = input('Password:')
    #输入收件人地址:
    to_addr = input('To:')
    #输入 SMTP 服务器地址:
    smtp_server = input('SMTP server:')
    
    server = smtplib.SMTP(smtp_server,25) # SMTP 协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()

if __name__ == '__main__':
    main()




