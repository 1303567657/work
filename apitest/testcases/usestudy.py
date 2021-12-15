from apitest.common.getpost import baserequest
from apitest.conf.ddtexcel import DoExcel
import xlrd
import unittest
#from apitest.common.getpost import baserequest
from ddt import data,unpack,ddt #引用ddt
import requests
test_data = DoExcel(r'D:\work\study\pycharm\seleniumstudy\apitest\data\case.xlsx','one').get_data()
print(test_data)
@ddt
class testcase(unittest.TestCase):
    @data(*test_data)
    def test_0001(self,test_data):

        ss = baserequest()
        #     #time.sleep(1)
        res = ss.httpGetOrPost(test_data['method'], test_data['url'], test_data['data'].encode('utf-8'))

if __name__ == '__main__':
     unittest.main()
