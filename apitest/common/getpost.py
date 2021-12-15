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

        return res

    def httpGetOrPost(self, method, url, data):


        headers = {"Content-Type": "application/json"}
        if method == "get":

            mres=self.httpGet(url,data)
        else:# method == "post":

            mres = self.httpPost(url,data)
        return mres
    def saonian(self):
        url = "https://www.youxinpai.com/getHomeData?cityId=201"
        method = "post"
        data = {"clientSecret": "a123af4e331cf61c0324cd43cbc2135d", "accountId": "13590404631"}
        res=self.httpGetOrPost("post", url, data)
        print(res.text)

ss=baserequest()
aa=ss.saonian()
print(aa)
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



