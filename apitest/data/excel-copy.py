# coding=utf-8
import time

import xlrd

from apitest.common.getpost import baserequest
import unittest

data = xlrd.open_workbook("D:\work\study\pycharm\seleniumstudy\\apitest\data\case.xlsx")
#
#
excel_path = r'D:\work\study\pycharm\seleniumstudy\apitest\data\case.xlsx'
excelfile = xlrd.open_workbook(excel_path)  # ,formatting_info=True)
sheet_1 = excelfile.sheets()[0]
# print(sheet_1)
answer = []
pass_or_false = []
body = {}
headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2427.7 Safari/537.36"
           }


class Dispose_excel():
    def get_case_count(self):  # ,path):
        # excel_path =path#
        excel_path = r'D:\work\study\pycharm\seleniumstudy\apitest\data\case.xlsx'
        excelfile = xlrd.open_workbook(excel_path)
        sheet_1 = excelfile.sheets()[0]
        rows_count = sheet_1.nrows
        return rows_count



def apppp():
    ss = baserequest()
    hh = Dispose_excel()
    count = hh.get_case_count()
    for i in range(2, count-5):
        # print(sheet_1.row_values(i))
        method = sheet_1.row_values(i)[1]
        # 请求地址
        url = sheet_1.row_values(i)[2]
        # 请求参数
        data = sheet_1.row_values(i)[3]
        #print("zheshishishsh", method,url,data)
        time.sleep(2)
        res = ss.httpGetOrPost(method, url, data)

        # print(res.text)
        #time.sleep(2)


apppp()
Dispose_excel=Dispose_excel()

# class unittest(unittest.TestCase):
#     def test_0001(self):
#
#         ss=baserequest()
#         methods = Dispose_excel.get_case_count()
#         print("这是什么顶顶顶顶顶顶大啊啊",methods)
#         #res = ss.httpGetOrPost(methods[0],methods[1],methods[2])#"post", url, data)
#         #print(res.text)
#
# if __name__ == '__main__':
#     unittest.main()