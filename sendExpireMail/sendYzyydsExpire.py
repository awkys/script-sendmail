import random
import smtplib
import time
from email.mime.text import MIMEText


def send_email(receiver, count, password):
    # 接收方／发送方，接收方是一个list，可以接受多个数值
    sender = count

    contant = """<div dir="ltr">
        ﻿亲，<font color="darkred">您在本站的账号已过期!</font>
        <br><br>
        <font color="red">为不影响您正常使用，请及时登录网站购买套餐后使用。</font><br><br>
		续费请 <a href="https://www.yzyyds.xyz" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.yzyyds.xyz&amp;source=gmail&amp;ust=1638599219093000&amp;usg=AOvVaw1_o00JKGkAtJHfAIdy040a">登录官网</a>，点击首页<font color="red">'购买套餐'</font> 按钮<br> <br>
		续费后请<font color="red">稍等两分钟,</font>然后重新连接客户端 <br> <br>
		官方网址： <a href="https://www.yzyyds.xyz" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.yzyyds.xyz&amp;source=gmail&amp;ust=1638599219094000&amp;usg=AOvVaw2ZcvjoZ_OBnw_4TE1vJZHf">https://www.yzyyds.xyz</a><div class="yj6qo"></div><div class="adL"> <br> <br>
        有疑问，请联系网站右下角在线客服 <br> <br>
        <br> <br>
        ﻿柚子加速器 - 提供专业海外网站加速服务，稳定运行六年!
		<br><br>
		畅游Google, Youtube, Facebook, Twitter, Instagram, 谷歌学术等海外网站
		<br><br>
		支持 苹果（iphone, Mac），安卓，电脑等客户端
		<br><br>
        邮件发送时间：<font color="darkred">%s</font>
        """%(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


    # 拼接邮件内容
    message = MIMEText(contant, "html", "utf-8")
    message['Subject'] = "柚子加速器 - 账户过期提醒,邮件编号:%s"%(random.randint(10000, 100000))
    message['From'] = sender
    message['To'] = receiver

    try:
        # tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
        smtp = smtplib.SMTP('smtp.office365.com', 587)
        smtp.set_debuglevel(True)
        # smtp.ehlo()
        smtp.starttls()
        # smtp.ehlo()
        smtp.login(count, password)
        smtp.sendmail(sender, [receiver], message.as_string())
        smtp.close()

    except smtplib.SMTPException:
        print(receiver)

if __name__ == '__main__':
    f = open("/var/sendMail/script/data/yzyyds521Expire.txt", "r")
    # f = open("../data/unSignUser.txt", "r")
    lines = f.readlines()
    for i in range(0, len(lines) - 1, 5):
        send_email(lines[i], 'tnmcer@outlook.com', 'Endc98765')
        time.sleep(random.uniform(432, 450))
        send_email(lines[i + 1], 'scmnvr@outlook.com', 'Huin123456')
        time.sleep(random.uniform(420, 445))
        send_email(lines[i + 2], 'uterncv@outlook.com', 'Tiun123456')
        time.sleep(random.uniform(410, 460))
        send_email(lines[i + 3], 'iurtdcd@outlook.com', 'Tiun123456')
        time.sleep(random.uniform(400, 455))
        send_email(lines[i + 4], 'uternbr@outlook.com', 'Tiun123456')
        time.sleep(random.uniform(405, 445))




