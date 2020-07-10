 # -*- coding: utf-8 -*-
import unittest
#from test_project.log.HTMLTestRunner import *
import time,os,datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from test_project.public.constant import CASE_PATH
from test_project.public.constant import REPORT_PATH

case_path = os.path.join(os.getcwd(),CASE_PATH)
report_path = os.path.join(os.getcwd(),REPORT_PATH )
print(case_path)
# 取test_case文件夹下所有用例文件
def creatsuitel(lists):
    testunit = unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(lists, pattern='test_*.py', top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit


#取前面时间加入到测试报告文件名中
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
filename = "report\\"+now+'result.html' #定义个报告存放路径，支持相对路径。
fp = open(filename, 'wb') #py3 open py2 file
runner = HTMLTestRunner(stream=fp, title='Report_title', description='Report_description')

if __name__ == "__main__":
    # 跑全部用例
    runner.run(creatsuitel(case_path))
    # 执行测试用例集并生成报告
    runner = unittest.TextTestRunner()

