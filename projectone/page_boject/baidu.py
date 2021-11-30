#coding=utf-8
import sys
import time
sys.path.append('..')
from selenium.webdriver.support.select import Select
from selenium import webdriver
#from projectone.base.base_page import BasePage
from base.base_page import BasePage
from selenium.webdriver.common.by import By
class xuanting(BasePage):
    url="https://www.baidu.com"
    #driver=webdriver.Chrome()
    xuanbutton=(By.XPATH,'//*[@id="s-usersetting-top"]')
    search=(By.XPATH,'//*[@id="kw"]')
    cli=(By.XPATH,'//*[@id="su"]')
    xuanz=(By.XPATH,'//*[@id="s-user-setting-menu"]/div/a[2]')
    def clickone(self):
        #self.visit(self.url)
        self.visit()
        self.driver.maximize_window()
        self.wait(1)
        self.xuan(self.xuanbutton)
        self.wait(2)

        #self.driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[2]').click()
        self.click(self.xuanz)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div/div/ul/li[1]').click()

    def searchs(self, sear):
        self.visit()
        self.driver.maximize_window()
        self.wait(1)
        self.xuan(self.xuanbutton)
        self.input(self.search, sear)
        self.click(self.cli)

if __name__=='__main__':
    driver=webdriver.Chrome()
    bai="手机"
    c=xuanting(driver)
    c.clickone()
    time.sleep(2)
    c.searchs(bai)


