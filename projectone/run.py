#coding=utf-8
import pytest
import os
if __name__=="__main__":
    pytest.main(['-s','./test_case/test_pystudy.py','--alluredir','./allure-results'])
    #os.system('allure.generate ./allure-results -o ./reports')
    os.system('allure generate ./allure-results -o ./report --clean')