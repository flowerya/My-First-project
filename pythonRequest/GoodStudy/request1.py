import pytest
import requests
class TestLogin:
    counts_data = [
        {
            "email": "yangyu@reddio.com",
            "password": "Lovexiang1314",
            "remember_me": "true"
        },
        {
            "email": "yangyu@reddio.co",
            "password": "Lovexiang1314",
            "remember_me": "true"
        },
        {
            "email": "yangyu@reddio.com",
            "password": "Lovexiang131",
            "remember_me": "true"
        }
    ]

    @pytest.mark.parametrize("account", counts_data)
    def testLogin(self,account):
        print(account,type(account))
        #接口地址 https://api-dev.reddio.com/v1/login
        url ='https://api-dev.reddio.com/v1/login'
        response = requests.post(url,account)
        response_json = response.json()
        #查看响应数据，返回的json，字典
        print(response.json())
        #获取token
        token = response_json.get("data")
        print(token)







