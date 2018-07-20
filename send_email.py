from email.mime.text import MIMEText  # 邮件文本转换
import smtplib  # 发送邮件
import time
#from Config import *


def Send_Email(accept_email, SMTP_server, Sender, password):
    print('邮箱开始发送...')
    # 三个参数：第一个为文本内容，第二个设置发送文本格式plain，第三个被文件utf-8 设置编码
    msg = MIMEText('票已经抢到，尽快付款')  # 转为邮件文本,
    msg["Subject"] = "票得到啦"  # 标题
    msg["From"] = Sender  # 发送者

    mail_sever = smtplib.SMTP(SMTP_server, 25)  # 链接邮箱端，端口号25

    mail_sever.login(Sender, password)  # 登录邮箱
    # 要发送的邮箱号
    email_list = [accept_email]
    for EMAIL in email_list:
        mail_sever.sendmail(Sender, EMAIL, msg.as_string())

    # 关闭邮箱
    mail_sever.quit()
    print("邮箱发送成功 ")

for i in range(0, 3):
    Send_Email(['531315901@qq.com', 'zhjuanhappy202@163.com'], "smtp.163.com" , 'zhjuanhappy@163.com', '1234qwer')
    time.sleep(3)