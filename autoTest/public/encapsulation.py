 # -*- coding: utf-8 -*-
# 封装部分维护在此
from config.config import locat_config
from log.log import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UIHandle():
    logger = Logger()

    # 构造方法，用来接收selenium的driver对象
    @classmethod
    def __init__(cls, driver):
        cls.driver = driver

    # 输入地址
    @classmethod
    def get(cls, url):
        cls.logger.loginfo(url)
        cls.driver.get(url)

    # 关闭浏览器驱动
    @classmethod
    def quit(cls):
        cls.driver.quit()

    # send_keys方法
    @classmethod
    def Input(cls, page, element, msg):
        el = cls.element(page, element)
        el.send_keys(msg)

    # click方法
    @classmethod
    def Click(cls, page, element):
        el = cls.element(page, element)
        el.click()

    #清除文本信息
    @classmethod
    def Clear(cls, page, element):
        el = cls.element(page, element)
        el.clear()

    #获取文本
    @classmethod
    def GetText(cls,page,element):
        el = cls.element(page, element)
        return el.text


    #获取属性值
    @classmethod
    def GetProperty(cls,page,element,property):
        el = cls.element(page, element)
        return el.get_attribute(property)

    #获取select

    # element对象（还可加入try，截图等。。。）
    @classmethod
    def element(cls, page, element):
       # 加入日志
       cls.logger.loginfo(page)
       # 加入隐性等待
       # 此处便可以传入config_o1中的dict定位参数
       el = WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located(locat_config[page][element]))
       # 加入日志
       cls.logger.loginfo(page+'OK')
       return el

    # element对象(还未完成。。。)
    def elements(cls, page, element):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入隐性等待
        WebDriverWait(cls.driver, 10)
        els = cls.driver.find_elements(*locat_config[page][element])
        # 注意返回的是list
        return els
