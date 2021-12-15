#from apitest.common.getpost import baserequest
import time
import unittest
import pytest,sys
from apitest.common.getpost import baserequest
sys.path.append('..')
#import unittest
from apitest.conf.excel import Dispose_excel
hh = Dispose_excel()
coun=hh.get_case_count(r'D:\work\study\pycharm\seleniumstudy\apitest\data\case.xlsx')
print(coun)
rows_count = coun.nrows
#rows_counts=Dispose_excel().get_case_count(r'D:\work\study\pycharm\seleniumstudy\apitest\data\case.xlsx')
class AAAunittestone(unittest.TestCase):
    def test_0001(self):
        for i in range(2, rows_count - 1):
            # print(sheet_1.row_values(i))

            method = coun.row_values(i)[1]
            url = coun.row_values(i)[2]
            #      #请求参数
            data = coun.row_values(i)[3]
            #print(method)
            ss=baserequest()
            #time.sleep(1)
            res = ss.httpGetOrPost(method, url, data)
            print(res.request)
    def test_0002(self):
        for i in range(2, rows_count - 1):
            # print(sheet_1.row_values(i))

            method = coun.row_values(i)[1]
            url = coun.row_values(i)[2]
            #      #请求参数
            data = coun.row_values(i)[3]
            #print(method)
            ass=coun.row_values(i)[4]
            ss=baserequest()
            #time.sleep(1)
            res = ss.httpGetOrPost(method, url, data)
            self.assertEqual(ass,200)
            print(res.request)
if __name__ == '__main__':
     unittest.main(verbosity=2)