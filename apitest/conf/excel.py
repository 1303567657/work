# coding=utf-8
import time
import xlrd
class Dispose_excel():
    def get_case_count(self,path):
        excel_path =path#
        #excel_path=r'D:\work\study\pycharm\seleniumstudy\apitest\data\case.xlsx'
        excelfile = xlrd.open_workbook(excel_path)  # ,formatting_info=True)
        sheet_1 = excelfile.sheets()[0]
        return sheet_1




        #下面的是学习的东西
        # 多少行
        #print(rows_count)
        #ows_count = sheet_1.nrows
        # for i in range(2, rows_count - 2):
        #      #print(sheet_1.row_values(i))
        #      method = sheet_1.row_values(i)[1]
        #      #请求地址
        #      url=sheet_1.row_values(i)[2]
        #      #请求参数
        #      data = sheet_1.row_values(i)[3]
        #      #print("zheshishishsh", method,url,data)






'''
#data = xlrd.open_workbook("D:\work\study\pycharm\seleniumstudy\\apitest\data\case.xlsx")
#
#
#excel_path = r'D:\work\study\pycharm\seleniumstudy\apitest\data\case.xlsx'
#excelfile = xlrd.open_workbook(excel_path)  # ,formatting_info=True)
#sheet_1 = excelfile.sheets()[0]
'''
# print(sheet_1)
answer = []
pass_or_false = []
body = {}
headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2427.7 Safari/537.36"
           }



             #return rows_count,method,url,data,


#hh = Dispose_excel()
#ss=hh.get_case_count()
#print(ss)

'''
class Dispose_excel():
    def get_case_count(self,path):
        excel_path =path#
        #excel_path=r'D:\work\study\pycharm\seleniumstudy\apitest\data\case.xlsx'
        excelfile = xlrd.open_workbook(excel_path)  # ,formatting_info=True)
        sheet_1 = excelfile.sheets()[0]
        #多少行
        rows_count = sheet_1.nrows
        #下面的是学习的东西
        print(rows_count)
        # for i in range(2, rows_count - 2):
        #      #print(sheet_1.row_values(i))
        #      method = sheet_1.row_values(i)[1]
        #      #请求地址
        #      url=sheet_1.row_values(i)[2]
        #      #请求参数
        #      data = sheet_1.row_values(i)[3]
        #      #print("zheshishishsh", method,url,data)

        return sheet_1'''
# def apppp():
#     ss = baserequest()
#     count = hh.get_case_count()
#     for i in range(2, count):
#         # print(sheet_1.row_values(i))
#         method = sheet_1.row_values(i)[1]
#         # 请求地址
#         url = sheet_1.row_values(i)[2]
#         # 请求参数
#         data = sheet_1.row_values(i)[3]
#         print("zheshishishsh", method,url,data)
#         #time.sleep(2)
#         res = ss.httpGetOrPost(method, url, data)
#
#         print(res.text)
#         time.sleep(2)
# apppp()

# class unittest(unittest.TestCase):
#     def test_0001(self):
#
#         ss=baserequest()
#         methods = hh.get_case_count()
#         print("这是什么顶顶顶顶顶顶大啊啊",methods)
#         res = ss.httpGetOrPost(methods[0],methods[1],methods[2])#"post", url, data)
#         #print(res.text)
#
# if __name__ == '__main__':
#     unittest.main()








# def use():
#     methods=hh.get_case_count()
#
#     print(methods)
# use()


###################################
#网络教材
'''
rows_count=sheet_1.nrows
        print(rows_count)
        for i in range(2,rows_count-3):
            print(sheet_1.row_values(i))
            ss=sheet_1.row_values(i)[1]
            print("zheshishishsh",ss)
            #pass
        #根据单元格获取
        cell_A1 = sheet_1.cell(0, 0).value
        print("fghjhjk",cell_A1)
        # 一共多少列
        ncols_count = sheet_1.ncols
        print(ncols_count)
        for i in range(1,ncols_count-5):
            #print(sheet_1.col_values(i))
            pass
        # 去掉表头 一共有多少个case
        real_count = rows_count - 1
        print(real_count)

        return real_count

'''
