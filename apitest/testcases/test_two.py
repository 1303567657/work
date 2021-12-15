#from apitest.common.getpost import baserequest
import time
import unittest
from ddt import ddt,file_data,data
import pytest,sys
import xlrd
from apitest.common.getpost import baserequest

sys.path.append('..')
#import unittest
from apitest.conf.excel import Dispose_excel
hh = Dispose_excel()
coun=hh.get_case_count(r'D:\work\study\pycharm\seleniumstudy\apitest\data\case.xlsx')
print(coun)
rows_count = coun.nrows
@ddt
class AAAunittesttwo(unittest.TestCase):
    @file_data(r'D:\work\study\pycharm\seleniumstudy\apitest\data\testcase.yaml')
    def test_0001(self,method,id,saonian):
        # for i in range(2, rows_count - 1):
        #     # print(sheet_1.row_values(i))
        #
        #     method = coun.row_values(i)[1]
        #     url = coun.row_values(i)[2]
        #     #      #请求参数
        #     data = coun.row_values(i)[3]
        #     #print(method)
        ss=baserequest()
        #     #time.sleep(1)
        res = ss.httpGetOrPost(method, id, saonian)
        print(res.content)

if __name__ == '__main__':
     unittest.main()
