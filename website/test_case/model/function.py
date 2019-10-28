from selenium import webdriver
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
import os


def insert_img(driver, fileName):
    """
    截图保存功能
    :param driver:初始化selenium webdriver对象
    :param fileName:文件路径和文件名
    :return:
    """
    # 获取当前模块路径
    func_Path = os.path.dirname(__file__)
    # 获取当前目录的上上级目录
    func_Path = os.path.dirname(os.path.dirname(func_Path))
    # 转化字符串
    func_Path = str(func_Path)
    # 转化字符串的双反斜杠
    func_Path = func_Path.replace('\\', '/')
    # 拼接图片存放位置和名字
    image_path = func_Path + r"/test_report/screenShot/" + fileName
    # 将截图保存到相应的路劲中
    driver.get_screenshot_as_file(image_path)


def latest_report(report_dir):
    """
    获取最新报告文件及位置
    :param report_dir: 报告位置
    :return:
    """
    # 获取指定文件夹下的所有目录
    lists = os.listdir(report_dir)
    # 对文件夹中的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir+'\\'+fn))
    # 获取文件夹中的最新文件
    file = os.path.join(report_dir, lists[-1])
    # 将得到的时间戳格式化
    # for i in range(len(lists)):
    #     n = os.path.getatime(report_dir + "\\" + lists[i])
    #     ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(n))
    return file


def send_email(latest_report):
    """
    邮件发送
    :param latest_report: 获取最后一个报告
    :return:
    """
    # 打开文件并读取传入文件夹中信心
    with open(latest_report,'rb') as f:
        mail_content = f.read()

    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱的用户名和授权密码
    user = 'yangleizi1020@163.com'
    password = 'yl0115'
    # 发送和接收邮箱
    sender = 'yangleizi1020@163.com'
    receives = ['1429895068@qq.com', 'yanglei10200115@163.com']
    # 发送邮件主题和内容
    subject = 'Web子系统自动化测试报告'
    # content = '<html><h1 style="color:red">我要自学网，自学成才</h1></html>'

    # 构建附件内容
    send_file = open(latest_report, 'rb').read()
    att = MIMEText(send_file, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename="latest_report.html"'

    msgRoot = MIMEMultipart()
    # HTML邮件正文
    msgRoot.attach(MIMEText(mail_content, 'html', 'utf-8'))
    msgRoot['Subject'] = Header(subject, 'utf-8')
    msgRoot['From'] = sender
    msgRoot['To'] = ','.join(receives)
    msgRoot.attach(att)
    # SSL协议端口号要使用465
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    # 向服务器表示用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)
    print("开始发送邮件！...")
    smtp.sendmail(sender, receives, msgRoot.as_string())
    smtp.quit()
    print("邮件发送完成！...")


if __name__ == '__main__':
    # driver = webdriver.Chrome()
    # driver.get('https://www.baidu.com')
    # insert_img(driver, 'd.png')

    send_email(latest_report(r'D:\youdankeji\website\test_report\screenShot'))
