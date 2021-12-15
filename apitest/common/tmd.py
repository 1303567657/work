# coding=utf-8
import json

import requests
class baserequest():
    def __init__(self) -> None:
        pass

    def httpPost(self,url,data):


        res=requests.post(url=url,data=data)

        return res

    def httpGet(self, url, data):
        #headers = {"Content-Type": "application/json"}

        res = requests.get(url=url,params=data)
        responseJson = res.json()
        return responseJson

    def run_mian(self, method, url, data):

        if method == "get":

            mres=self.httpGet(url,data)
        else:

            mres = self.httpPost(url,data)
        return mres
if __name__=="__main__":
    url = "https://www.youxinpai.com/getHomeData?cityId=201"
    method = "post"
    data = {"clientSecret": "a123af4e331cf61c0324cd43cbc2135d", "accountId": "13590404631"}
    zidonghua=baserequest()
    res = zidonghua.run_mian("post", url, data)
    print(res.text)
        #zhttpGetOrPost("post", url, dataa)

'''
            elif method == "put":
            mres = requests.put(url, data=data, headers=headers)
        elif method == "delete":
            mres = requests.delete(url, data=data, headers=headers)
        else:
            mres = requests.post(url, data=data, headers=headers)
        print("错误")
        # responseJson=mres.json()
        return mres.json()
    '''



