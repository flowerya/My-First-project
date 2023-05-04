# 测试登录
import pytest
import requests
class TestLogin:
    counts_data = [
        {
            "email": "yangyu@reddio.com",
            "password": "Lovexiang1314",
            "remember_me": "true",
            "status": "OK"
        },
        {
            "email": "yangyu@reddio.co",
            "password": "Lovexiang1314",
            "remember_me": "true",
            "status": "FAILED"
        },
        {
            "email": "yangyu@reddio.com",
            "password": "Lovexiang131",
            "remember_me": "true",
            "status": "FAILED"
        }
    ]
    @pytest.mark.parametrize("account", counts_data)
    def testLogin(self,account):
        url ='https://api-dev.reddio.com/v1/login'
        user_name = account.get("email")
        password = account.get("password")
        remeber = account.get("remember_me")
        sta = account.get( "status")
        data={
            "email": user_name,
            "password":password ,
            "remember_me":  remeber,
        }
        response = requests.post(url,data)
        response_json = response.json()
        print(response.json())
        status = response_json.get("status")
        assert(status==sta)








