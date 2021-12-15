# coding=utf-8
import json
import requests
import unittest

class BaseRequests():
    def __init__(self) -> None:
        pass

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).text
        return res

    def send_get(self, url, data):
        res = requests.get(url=url, params=data).text
        print(res)
        return res

    def run_mian(self, method, url, data):
        if method == "get":
            res = self.send_get(url, data)

        else:
            res = self.send_post(url, data)
        return res

if __name__=="__main__":
    zidonghua = BaseRequests()
    url = "https://www.youxinpai.com/getHomeData?cityId=201"
    method = "post"
    data = {"password":"e10adc3949ba59abbe56e057f20f883e","clientSecret":"a123af4e331cf61c0324cd43cbc2135d","accountId":"13590404631"}
    #dataa = json.dumps(data)

    res = zidonghua.run_mian("post", url, data)
    print(res)

# url = "http://platform-auction-biz.svc.test.suixinhuan.com/auctionListController/getAuctionCarList.json"
# data = {
#     "pageType": 12,
#     "pageIndex": 1,
#     "pageSize": 1000,
#     "operationPosition": "UAu810Lf9H"
# }

data = json.dumps(data)
res = zidonghua.run_mian("post", url, data)
print(res)
'''


class ImoocCase(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)

    def test_list(self):
        url = "http://platform-auction-biz.svc.test.suixinhuan.com/auctionListController/getAuctionCarList.json"
        data = {
            "pageType": 12,
            "pageIndex": 1,
            "pageSize": 1000,
            "operationPosition": "UAu810Lf9H"
        }
        data = json.dumps(data)
        res = zidonghua("post", url, data)
        print(res)
        # 判断 接口返回数值
        self.assertEqual(res["code"], "200")


if __name__ == "_main_":
    unittest.main()
'''