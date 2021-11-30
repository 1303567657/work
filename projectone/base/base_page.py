#coding=utf-8
from time import sleep
#封装函数
from selenium import webdriver
from selenium.webdriver import ActionChains
class BasePage():
    #driver = webdriver.Chrome()
    def __init__(self,driver):
        self.driver=driver
    #访问url
    def visit(self):
        self.driver.get(self.url)
    #定位元素
    def locator(self,loc):
        return self.driver.find_element(*loc)
    #输入
    def input(self,loc,text):
        self.locator(loc).send_keys(text)
    #点击元素
    def click(self,loc):
        self.locator(loc).click()
    #鼠标悬停
    def xuan(self,loc):
        #xuan = b.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        xuanone=self.locator(loc)
        ActionChains(self.driver).move_to_element(xuanone).perform()
    #选择select
    def select(self):
        pass
    #等待
    def wait(self,time_):
        sleep(time_)
#print('saonian')



