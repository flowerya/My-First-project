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
    def test_Login(self,account):
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

    def test_GetToken(self):
        url = 'https://api-dev.reddio.com/v1/login'
        json = {
            "email": "yangyu@reddio.com",
            "password": "Lovexiang1314",
            "remember_me": "true",
        }
        response = requests.post(url, json)
        response_json = response.json()
        token = response_json.get("data").get("token")
        print(token)
        return token
    def test_GetUUID(self):
        url = 'https://api-dev.reddio.com/v1/project'
        token1 = self.GetToken()
        heads ={
        "Content-Type ":"application/json",
        "token":token1,
        "Access-Control-Allow-Methods ":"GET, POST, OPTIONS",
        }
        getResponse = requests.get(url,headers=heads)
        getResponse_json = getResponse.json()
        data =getResponse_json.get("data")
        project_uuid=data[1].get("project_uuid")
        print(project_uuid)









