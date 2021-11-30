#coding=utf-8
import time
import pytest,sys
sys.path.append('..')
import allure
#import  unittest
from ddt import ddt,file_data,data
import sys
from selenium.webdriver.chrome.options import Options
sys.path.append('D:\work\study\pycharm\seleniumstudy\projectone')
from  selenium import  webdriver
#from projectone.page_boject.baidu import xuanting
from page_boject.baidu import xuanting
#@ddt


class TestCase1(object):#unittest.TestCase):
    @classmethod
   # @allure.step("步骤1:点xxx")
    #def setUpClass(cls) -> None:
    def setup_class(cls):
        #设置展示浏览器使用这个
        #cls.driver = webdriver.Chrome()
        # cls.b = xuanting(cls.driver)
        #
        # cls.c = xuanting(cls.driver)
        #设置无头使用下面的
        cls.chrome_options = Options()
        cls.chrome_options.add_argument('--headless')
        cls.driver = webdriver.Chrome(chrome_options=cls.chrome_options, executable_path="chromedriver.exe")
        #return cls.driver
        cls.b = xuanting(cls.driver)

        cls.c = xuanting(cls.driver)

    @classmethod
    # @allure.step("步骤2:点xxx")
    def teardown_class(cls):
        #cls.driver = webdriver.Chrome()
        cls.driver.quit()
    def test_one(self):
         #driver = webdriver.Chrome()
         #bai = "手机"
         b = xuanting(self.driver)
         self.b.clickone()
         time.sleep(3)
    #@file_data(r'D:\work\study\pycharm\seleniumstudy\projectone\data\user.yaml')
    #@data(1,2)
    #@allure.story("测试点1")
    def test_twoo(self):
        #driver = webdriver.Chrome()
        bai = "手机"
        #c = xuanting(self.driver)
        self.c.searchs(bai)
        time.sleep(3)



#
# class TestCase(object):#unittest.TestCase):
#     @classmethod
#     #def setUpClass(cls) -> None:
#     def setup_class(cls):
#         cls.driver = webdriver.Chrome()
#         cls.b = xuanting(cls.driver)
#         cls.c = xuanting(cls.driver)
#
#     @classmethod
#     def teardown_class(cls):
#         cls.driver = webdriver.Chrome()
#         cls.driver.quit()
#     # def test_one(self):
#     #     #driver = webdriver.Chrome()
#     #     #bai = "手机"
#     #     #c = xuanting(driver)
#     #     self.b.clickone()
#     #     time.sleep(3)
#     #@file_data(r'D:\work\study\pycharm\seleniumstudy\projectone\data\user.yaml')
#     #@data(1,2)
#     #@allure.story("测试i点2")
#     def test_two(self):
#         #driver = webdriver.Chrome()
#         bai = "gjjj"
#         #c = xuanting(self.driver)
#         self.c.searchs(bai)
#         time.sleep(3)
#         self.driver.quit()

if __name__=='__main__':
   #unittest.main
   pytest.main()#['-s','-v', 'dian.py'])

