# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import *


# config配置部分

# 浏览器种类维护在此处
browser_config = {
    'ie': webdriver.Ie,
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}

# 定位信息维护在此处，维护结构由外到内为：页面名称--页面下元素名称--元素的定位方式+参数
locat_config = {
    '快问': {
        '登陆邮箱': ['name', 'email'],
        '登陆密码': ['name', 'password'],
        '登陆按钮': ['xpath', '/html/body/div[3]/form/div[3]/button'],
        '处方管理': ['xpath', '/html/body/div[3]/div[1]/div/ul/li[8]/a/span'],
        '处方列表': ['xpath', '/html/body/div[3]/div[1]/div/ul/li[8]/ul/li[1]'],
        '编辑表': {'xpath', '/html/body/div[3]/div[2]/div/div[1]/div/div/ul/li[2]'},
        '处方ID搜索框': ['xpath', '//*[@id="prescriptionList"]/thead/tr[2]/td[1]/input'],
        '处方搜索按钮': ['xpath', '//*[@id="prescriptionList"]/thead/tr[2]/td[20]/div/button'],
        '处方编辑按钮': ['xpath', '//*[@id="prescriptionList"]/tbody/tr/td[20]/a[1]'],
        '用户手机': ['xpath', '//*[@id="baseInfo"]/div[3]/div[2]/div/div/input'],
        '关联患者': ['xpath', '//*[@id="relatePatientInfo"]'],
        '处方剂量': ['xpath', '//*[@id="baseInfo"]/div[5]/div[2]/div/div/input[2]'],
        '处方制法': ['id', 'selectManu'],
        '地址下拉框': ['id', 's2id_selectProvince'],
        '省份': ['id', 's2id_selectProvince'],
        '广东省': ['id', 'select2-result-label-35'],
        '城市': ['id', 's2id_selectCity'],
        '广州市': ['xpath', '//*[@id="select2-results-36"]/li[21]'],
        '区域': ['id', 's2id_selectZone'],
        '海珠区': ['xpath', '//*[@id="select2-results-59"]/li[2]'],
        '保存按钮': ['xpath', '//*[@id="infoForm"]/div[1]/div/div/button'],
        '地址': ['xpath', '//div/div[4]/div[1]/textarea'],
        '完成处方编辑': ['xpath', '//*[@id="done"]'],
        '确定完成编辑': ['xpath', '/html/body/div[4]/div[2]/div/div[2]/button[2]'],
        '等待付款':['xpath','/html/body/div[3]/div[2]/div/div[1]/div/div/ul/li[3]/a'],
        '等待付款搜索':['xpath','//*[@id="prescriptionList"]/thead/tr[2]/td[21]/div/button'],
        '银行卡付款':['xpath','//*[@id="prescriptionList"]/tbody/tr/td[21]/a[6]'],
        '货到付款确认按钮':['xpath','/html/body/div[4]/div[2]/div/div[2]/button[2]'],
        '收款确认':['xpath','/html/body/div[3]/div[2]/div/div[2]/div/div/ul/li[5]/a'],
        '退出':['xpath','/html/body/div[1]/div/div[2]/ul/li/ul/li[3]/a'],
        '药房处方列表':['xpath','/html/body/div[3]/div[1]/div/ul/li[4]/a/span'],
        '订单ID搜索框':['xpath','//*[@id="prescriptionList"]/thead/tr[2]/td[1]/input'],
        '订单搜索按钮':['xpath','//*[@id="prescriptionList"]/thead/tr[2]/td[10]/div/button'],
        '打印预览':['xpath','//*[@id="prescriptionList"]/tbody/tr/td[10]/a[2]'],
        '患者打印留底':['xpath','//*[@id="printBtnWrapper"]/button[2]'],
    },
    '测试':{
        '搜索框':['xpath','//*[@id="kw"]'],
    }
}
