# -*- coding: utf-8 -*-
from public.constant import *
from selenium.webdriver.support.select import Select
from time import sleep
from db.connectDB import dbUtil
from config.config import *
import os
import re
# 业务功能脚本（用例脚本可调用此处的功能脚本）

# 登陆


class Login():

    # 登陆
    def kw_login(self):
        email = input("请输入邮箱:")
        password = input("请输入密码:")

        # 调用二次封装后的方法，此处可见操作了哪个页面，哪个元素，msg是要插入的值，插入值得操作在另外一个用例文件中传入
        self.uihandle.Input('快问', '登陆邮箱', email)
        self.uihandle.Input('快问', '登陆密码', password)
        self.uihandle.Click('快问', '登陆按钮')
# 退出


class Quit():
    def kw_quit(self):
        self.uihandle.get(KW_LOGOUT_URL)

# v1: 对指定ID的处方进行处理：登录-新建-已发货
# v2: 对指定ID的处方发送到不同药房进行处理
# v3: 拆单处理


class Prescription():
    # 选择列表
    def kw_selectList(self):
        self.uihandle.Click('快问', '处方管理')
        self.uihandle.Click('快问', '处方列表')

    # 选择表
    def kw_selectTable(self):
        self.uihandle.Click('快问', '编辑表')

    # 查询处方ID
    def kw_selectPrescribe(self, id):
        self.uihandle.Input('快问', '处方ID搜索框', id)
        self.uihandle.Click('快问', '处方搜索按钮')
    # 编辑处方

    def kw_clickEdit(self):
        self.uihandle.Click('快问', '处方编辑按钮')

    def kw_finishEdit(self):
        if self.uihandle.GetText('快问', '用户手机') == '0':
            # 用户手机号为空默认填写13692714849
            self.uihandle.Input('快问', '用户手机', '13692714849')
            self.uihandle.Click('快问', '关联患者')
            #value = self.driver.find_element_by_xpath('//*[@id="baseInfo"]/div[5]/div[2]/div/div/input[2]').get_attribute('value')
            #value = self.uihandle.GetProperty('快问', '处方剂量', 'value')
            # if value == '0':
            if self.uihandle.GetProperty(
                    '快问', '处方剂量', 'value') == '0' or self.uihandle.GetProperty(
                    '快问', '处方剂量', 'value') == '':
                # 若处方剂量为0 添加为1
                self.uihandle.Clear('快问', '处方剂量')
                self.uihandle.Input('快问', '处方剂量', '1')
            #preparation = Select(self.driver.find_element_by_id('selectManu')).first_selected_option.text
            if Select(self.driver.find_element_by_id('selectManu')
                      ).first_selected_option.text == '请选择制法':
                # 若未选择制法则默认选择自煎
                self.uihandle.Click('快问', '处方制法')
                Select(self.driver.find_element_by_id(
                    'selectManu')).select_by_value('1')

            #province = self.driver.find_element_by_id('s2id_selectProvince').text
            #province = self.uihandle.GetText('快问','地址下拉框')
            # if province == '选择省份':
            if self.uihandle.GetText('快问', '地址下拉框') == '选择省份':
                # 若未填地址默认选择广东省广州市海珠区
                self.uihandle.Click('快问', '省份')
                self.uihandle.Click('快问', '广东省')
                sleep(2)
                self.uihandle.Click('快问', '城市')
                self.uihandle.Click('快问', '广州市')
                sleep(2)
                self.uihandle.Click('快问', '区域')
                self.uihandle.Click('快问', '海珠区')

            #address = self.driver.find_element_by_xpath('//*[@id="baseInfo"]/div[10]/div/div[4]/div[1]/textarea').text
            #address = self.uihandle.GetText('快问','地址')
            # if address =='':
            if self.uihandle.GetText('快问', '地址') == '':
                self.uihandle.Input('快问', '地址', '默认地址')

        else:
            if self.uihandle.GetProperty(
                    '快问', '处方剂量', 'value') == '0' or self.uihandle.GetProperty(
                    '快问', '处方剂量', 'value') == '':
                self.uihandle.Clear('快问', '处方剂量')
                self.uihandle.Input('快问', '处方剂量', '1')
            if Select(self.driver.find_element_by_id('selectManu')
                      ).first_selected_option.text == '请选择制法':
                self.uihandle.Click('快问', '处方制法')
                Select(self.driver.find_element_by_id(
                    'selectManu')).select_by_value('1')

            if self.uihandle.GetText('快问', '地址下拉框') == '选择省份':
                self.uihandle.Click('快问', '省份')
                self.uihandle.Click('快问', '广东省')
                sleep(1)
                self.uihandle.Click('快问', '城市')
                self.uihandle.Click('快问', '广州市')
                sleep(1)
                self.uihandle.Click('快问', '区域')
                self.uihandle.Click('快问', '海珠区')
            sleep(1)
            if self.uihandle.GetText('快问', '地址') == '':
                self.uihandle.Input('快问', '地址', '默认地址')

        self.uihandle.Click('快问', '保存按钮')
        # 获取草药
        herbalMedicines = self.driver.find_element_by_xpath(
            '//*[@id="herbListBody"]').find_elements_by_tag_name('tr')
        if len(herbalMedicines) != 0:
            sleep(0.5)
            Pharmacy = Select(self.driver.find_element_by_xpath(
                '//*[@id="herbPharmacyId"]')).first_selected_option.text
            if Pharmacy == '选择草药药房':
                Select(self.driver.find_element_by_name(
                    'pharmacy_id')).select_by_value('44')
        # print(list[0].find_elements_by_tag_name('td')[0].text)

        # 获取协定方
        prescriptions = self.driver.find_element_by_xpath(
            '//*[@id="productListBody"]').find_elements_by_tag_name('tr')
        # self.driver.find_element_by_xpath('//*[@id="productListBody"]').find_elements_by_tag_name('tr')[0].click()
        if len(prescriptions) != 0:
            #     for prescription in prescriptions:
            # if prescription.find_elements_by_tag_name('td')[5].text =='选择药房':

                    #searchButton = prescription.find_elements_by_tag_name('td')[5]
                    # self.driver.execute_script("arguments[0].click();", searchButton);
                    # #self.driver.execute_script('prefpanelgo")[0].click()',prescription.find_elements_by_tag_name('td')[5])
                    # searchButton.click()
                    # searchButtons = self.driver.find_elements_by_xpath('//table/tbody/tr/td[6]/a')

            searchButtons = self.driver.find_elements_by_css_selector(
                '.product-pharmacy.editable.editable-click')

            for searchButton in searchButtons:
                if searchButton.text == '选择药房':
                    searchButton.click()
                    sleep(1)
                    Select(self.driver.find_element_by_css_selector(
                        '.form-control.input-medium')).select_by_value('2')
                    self.driver.find_element_by_xpath(
                        '//div[2]/div/form/div/div[1]/div[2]/button[1]').click()

        flag = False
        # 获取中成药
        proprietarys = self.driver.find_element_by_id(
            'herbPharmacyId').find_elements_by_tag_name('tr')
        if len(proprietarys) != 0:
            for proprietary in proprietarys:
                if proprietary.find_elements_by_tag_name('td')[
                        6].text == '选择药房':
                    flag = True
                    break
        if flag:
            self.driver.find_element_by_xpath(
                '//*[@id="splitMedicines"]').Click()
            self.driver.find_element_by_xpath(
                '/html/body/div[6]/div[2]/div/div[2]/button[2]').Click()

        sleep(1)
        self.uihandle.Click('快问', '完成处方编辑')
        sleep(1)
        self.uihandle.Click('快问', '确定完成编辑')
        sleep(1)
        s = len(self.driver.find_elements_by_css_selector(
            '.Metronic-alerts.alert.alert-danger.fade.in'))
        if s != 0:
            print(self.driver.find_elements_by_css_selector(
                '.Metronic-alerts.alert.alert-danger.fade.in')[0].text)
    # 等待付款

    def kw_payment(self, id):
        self.uihandle.Click('快问', '等待付款')
        self.uihandle.Input('快问', '处方ID搜索框', id)
        sleep(0.5)
        self.uihandle.Click('快问', '等待付款搜索')
        self.uihandle.Click('快问', '银行卡付款')
        sleep(0.5)
        self.uihandle.Click('快问', '货到付款确认按钮')
    # 发货

    def kw_Send(self, id):
        self.uihandle.Click('快问', '收款确认')
        # s = len(self.driver.find_elements_by_xpath(
        #     '/html/body/div[3]/div[2]/div/div[1]/a'))
        # if s != '0':
        #     print(self.driver.find_elements_by_xpath(
        #         '/html/body/div[3]/div[2]/div/div[1]/a')[0].text)
        self.uihandle.Input('快问', '处方ID搜索框', id)
        self.uihandle.Click('快问', '等待付款搜索')

        type = self.driver.find_element_by_xpath(
            '//*[@id="prescriptionList"]/tbody/tr/td[21]/a[1]').text
        # 拆分订单
        # 要优化
        if type == '拆分订单':
            self.driver.find_element_by_xpath(
                '//*[@id="prescriptionList"]/tbody/tr/td[21]/a[1]').click()
            sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/button[2]').click()
            dbUtil.coonDB(self)
            sql = 'select id,pharmacy_id from prescriptions where parent_id = ' + str(id)
            rows= dbUtil.Select(self,sql)
            dbUtil.closeDB(self)
            for row in rows:
                orderid = re.sub(r'\(|\)|,',"",str(row[0]))
                self.uihandle.Clear('快问', '处方ID搜索框')
                self.uihandle.Input('快问', '处方ID搜索框',orderid)
                self.uihandle.Click('快问', '等待付款搜索')

                type = self.driver.find_element_by_xpath(
                    '//*[@id="prescriptionList"]/tbody/tr/td[21]/a[1]').text

                if type == '选择药房':
                    self.driver.find_element_by_xpath(
                        '//*[@id="prescriptionList"]/tbody/tr/td[21]/a[1]').click()
                    if Select(self.driver.find_element_by_id('pharmacySel')
                              ).first_selected_option.text == '选择药房':
                        Select(self.driver.find_element_by_id(
                            'pharmacySel')).select_by_value('2')
                    self.driver.find_element_by_xpath(
                        '//*[@id="choosePharmacy"]/div[2]/div/div/a[1]').click()
                    sleep(1)
                    self.driver.find_elements_by_css_selector(
                        '.btn.btn-primary')[0].click()
                else:
                    info = self.driver.find_element_by_xpath(
                        '//*[@id="prescriptionList"]/tbody/tr/td[21]/a[3]').text
                    if info == '发送到至信药业（至信）':
                        self.driver.find_element_by_xpath(
                            '//*[@id="prescriptionList"]/tbody/tr/td[21]/a[3]').click()
                        if Select(self.driver.find_element_by_name('is_within')
                                  ).first_selected_option.text == '请选择':
                            Select(self.driver.find_element_by_name(
                                'is_within')).select_by_value('1')
                        self.driver.find_element_by_xpath(
                            '//*[@id="kmInfo"]/div[2]/div/div/a[1]').click()
                        sleep(1)
                        self.driver.find_elements_by_css_selector(
                            '.btn.btn-primary')[0].click()
                    elif info == '发送至康美(广州)':
                        self.driver.find_element_by_xpath(
                            '//*[@id="prescriptionList"]/tbody/tr/td[21]/a[3]').click()
                        if Select(self.driver.find_element_by_name('is_within')
                                  ).first_selected_option.text == '请选择':
                            Select(self.driver.find_element_by_name(
                                'is_within')).select_by_value('1')
                        self.driver.find_element_by_xpath(
                            '//*[@id="kmInfo"]/div[2]/div/div/a[1]').click()
                        sleep(1)
                        self.driver.find_elements_by_css_selector(
                            '.btn.btn-primary')[0].click()
                    else:
                        print("不是至信药业（至信）或康美(广州)")
                self.uihandle.Click('快问', '收款确认')
            return rows


        # 选择药房
        elif type == '选择药房':
            self.driver.find_element_by_xpath(
                '//*[@id="prescriptionList"]/tbody/tr/td[21]/a[1]').click()
            if Select(self.driver.find_element_by_id('pharmacySel')
                      ).first_selected_option.text == '选择药房':
                Select(self.driver.find_element_by_id(
                    'pharmacySel')).select_by_value('2')
            self.driver.find_element_by_xpath(
                '//*[@id="choosePharmacy"]/div[2]/div/div/a[1]').click()
            sleep(1)
            self.driver.find_elements_by_css_selector(
                '.btn.btn-primary')[0].click()
        # 发送药房 香雪发不出去 不考虑 就考虑至信的情况

        else:
            info = self.driver.find_element_by_xpath(
                '//*[@id="prescriptionList"]/tbody/tr/td[21]/a[3]').text
            if info == '发送到至信药业（至信）':
                self.driver.find_element_by_xpath(
                    '//*[@id="prescriptionList"]/tbody/tr/td[21]/a[3]').click()
                if Select(self.driver.find_element_by_name('is_within')
                          ).first_selected_option.text == '请选择':
                    Select(self.driver.find_element_by_name(
                        'is_within')).select_by_value('1')
                self.driver.find_element_by_xpath(
                    '//*[@id="kmInfo"]/div[2]/div/div/a[1]').click()
                sleep(1)
                self.driver.find_elements_by_css_selector(
                    '.btn.btn-primary')[0].click()
            elif info == '发送至康美(广州)':
                self.driver.find_element_by_xpath(
                    '//*[@id="prescriptionList"]/tbody/tr/td[21]/a[3]').click()
                if Select(self.driver.find_element_by_name('is_within')
                          ).first_selected_option.text == '请选择':
                    Select(self.driver.find_element_by_name(
                        'is_within')).select_by_value('1')
                self.driver.find_element_by_xpath(
                    '//*[@id="kmInfo"]/div[2]/div/div/a[1]').click()
                sleep(1)
                self.driver.find_elements_by_css_selector(
                    '.btn.btn-primary')[0].click()
            else:
                print("不是至信药业（至信）或康美(广州)")

    # 药房发货

    def kw_deliverGoods(self, rows):
        if isinstance(rows,str)==False:
            for row in rows:
                pharmacyId = re.sub(r'\(|\)|,', "", str(row[1]))
                if pharmacyId =='4':
                    orderid = re.sub(r'\(|\)|,', "", str(row[0]))
                    self.uihandle.Click('快问', '药房处方列表')
                    self.uihandle.Input('快问', '订单ID搜索框', '0' + orderid)
                    self.uihandle.Click('快问', '订单搜索按钮')
                    if self.driver.find_element_by_xpath(
                            '//*[@id="tab_1_1_1"]/div/div/div[2]/div[2]').text == '当前显示：1 / 1':
                        self.uihandle.Click('快问', '打印预览')
                    else:
                        print('搜索不到该订单ID')
                    # 获取打开的多个窗口句柄
                    windows = self.driver.window_handles
                    # 切换到当前最新打开的窗口
                    self.driver.switch_to.window(windows[-1])
                    self.uihandle.Click('快问', '患者打印留底')
                    self.driver.close()
        else:
            self.uihandle.Click('快问', '药房处方列表')
            self.uihandle.Input('快问', '订单ID搜索框', '0' + str(rows))
            self.uihandle.Click('快问', '订单搜索按钮')
            if self.driver.find_element_by_xpath(
                    '//*[@id="tab_1_1_1"]/div/div/div[2]/div[2]').text == '当前显示：1 / 1':
                self.uihandle.Click('快问', '打印预览')
            else:
                print('搜索不到该订单ID')
            # 获取打开的多个窗口句柄
            windows = self.driver.window_handles
            # 切换到当前最新打开的窗口
            self.driver.switch_to.window(windows[-1])
            self.uihandle.Click('快问', '患者打印留底')
            self.driver.close()
            sleep(2)
            # self.driver.close()
# class Test():
#
