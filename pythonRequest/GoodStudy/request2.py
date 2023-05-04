#获取token
import pytest
import requests
class TestEduitProject:
    def  testLogin(self):
        url = 'https://api-dev.reddio.com/v1/login'
        json = {
            "email": "yangyu@reddio.com",
            "password": "Lovexiang1314",
            "remember_me": "true",
        }
        response = requests.post(url,json)
        response_json = response.json()
        token = response_json.get("data").get("token")
        return token
    def testGetUUID(self):
        url = 'https://api-dev.reddio.com/v1/project'
        token1 = self.testLogin()
        heads ={
        "Content-Type ":"application/json",
        "token":token1,
        "Access-Control-Allow-Methods ":"GET, POST, OPTIONS",
        }
        print(token1)
        getResponse = requests.get(url,headers=heads)
        getResponse_json = getResponse.json()
        print (getResponse_json)
        data =getResponse_json.get("data")
        project_uuid=data[1].get("project_uuid")
        print(project_uuid)





