#coding=utf-8
import time
import pytest
import  unittest
from ddt import ddt,file_data,data
from  selenium import  webdriver
from projectone.page_boject.baidu import xuanting
@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.b = xuanting(cls.driver)
        cls.c = xuanting(cls.driver)


    # def test_one(self):
    #     #driver = webdriver.Chrome()
    #     #bai = "手机"
    #     #c = xuanting(driver)
    #     self.b.clickone()
    #     time.sleep(3)
    @file_data(r'D:\work\study\pycharm\seleniumstudy\projectone\data\user.yaml')
    #@data(1,2)
    def test_two(self,txt):
        #driver = webdriver.Chrome()
        #bai = "手机"
        #c = xuanting(self.driver)
        self.c.searchs(txt)
        time.sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.quit()
@ddt
class TestCase1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.b = xuanting(cls.driver)
        cls.c = xuanting(cls.driver)


    # def test_one(self):
    #     #driver = webdriver.Chrome()
    #     #bai = "手机"
    #     #c = xuanting(driver)
    #     self.b.clickone()
    #     time.sleep(3)
    #@file_data(r'D:\work\study\pycharm\seleniumstudy\projectone\data\user.yaml')
    @data(1,2)
    def test_two(self,txt):
        #driver = webdriver.Chrome()
        #bai = "手机"
        #c = xuanting(self.driver)
        self.c.searchs(txt)
        time.sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        cls.driver.quit()
if __name__=='__main__':
   unittest.main()

