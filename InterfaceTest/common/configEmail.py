#这个文件主要是配置发送邮件的主题、正文等，将测试报告发送并抄送到相关人邮箱的逻辑
from email.header import Header
import smtplib
from email.mime.text import MIMEText

def sendMail(text):
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '609853435@qq.com'
    password = 'vcevhmpudwwhbdcj'

    # 收信方邮箱
    to_addr = '13692714849@163.com'

    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(text, 'html', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('测试报告')

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL(host=smtp_server)

    server.connect(host=smtp_server,port=465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()
