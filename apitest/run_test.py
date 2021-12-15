import time
from BeautifulReport import BeautifulReport
import unittest
case_dir=r'D:\work\study\pycharm\seleniumstudy\apitest\testcases'
discover=unittest.defaultTestLoader.discover(case_dir,
                                             pattern='test*.py',
                                             top_level_dir=None)
if __name__=="__main__":
     #   suite = unittest.TestSuite()
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename =now + '_result.html'
    report_path=r'D:\work\study\pycharm\seleniumstudy\apitest\report\re'
    result=BeautifulReport(discover)
    result.report(filename=filename,description='测试报告思密达',log_path=report_path)

