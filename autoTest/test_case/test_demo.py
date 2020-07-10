# -*- coding: utf-8 -*-
import unittest
from public.function import *
from public.encapsulation import UIHandle
# 用例


class test_demo():
    def setUp(self):
        # 打开浏览器
        driver = browser_config['chrome']()
        # 传入driver对象
        uihandle = UIHandle(driver)

        # admin@kw13.cn c1ae8967-3570-4b15-a1e9-4ba3d11aa147
        # zxcs@kw13.cn 123456789

    def test_demo(self):
        print('123')
        self.uihandle.get(KW_LOGIN_URL)
        Login.kw_login( self)
        self.driver.maximize_window()
        Prescription.kw_selectList(self)
        id = input("请输入订单ID:")
        Prescription.kw_selectPrescribe(self,id)
        Prescription.kw_clickEdit(self)
        Prescription.kw_finishEdit(self)
        Prescription.kw_payment(self,id)
        rows = Prescription.kw_Send(self,id)
        Quit.kw_quit(self)
        self.uihandle.get(KW_LOGIN_URL)
        Login.kw_login(self)
        if rows ==None:
            Prescription.kw_deliverGoods(self, id)
        else:
            Prescription.kw_deliverGoods(self,rows)

        #------------------------------------------------------
        # self.uihandle.get(Test_URL)
        # self.uihandle.Input('测试','搜索框','万古神帝')



    def tearDown(self):
        sleep(3)
        self.uihandle.quit()
def main():
    test_demo.test_demo();

if __name__ == "__main__":
    main()
