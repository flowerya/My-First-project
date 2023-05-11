#获取token
import pytest
import requests
import Common.yaml_util


@pytest.fixture(scope='session', autouse=True)
def cleanYaml():
    Common.yaml_util.clean_Yaml()

class TestEduitProject:
    # aaccess_token='' 使用yaml文件读取写入替换掉
    access_session = requests.session()
    @pytest.mark.run(order=2)
    def  test_GetToken(self):
        url = 'https://api-dev.reddio.com/v1/login'
        data = {
            "email": "yangyu@reddio.com",
            "password": "Lovexiang1314",
            "remember_me": "true",
        }
        # response = requests.request(method='post',url=url,json=data)
        response = TestEduitProject.access_session.request(method='post', url=url, json=data)#通过session创建关联的会话

        response_json = response.json()
        token = response_json.get("data").get("token")
        # Common.yaml_util.clean_Yaml()##先做清空yaml操作
        Common.yaml_util.write_Yaml({"aaccess_token":token})##将token以数据流的形式写入yaml文件
        print(token);
        # TestEduitProject.aaccess_token = token
    @pytest.mark.run(order=3)
    def test_GetUUID1(self):
        url = 'https://api-dev.reddio.com/v1/project'
        # token1 = TestEduitProject.aaccess_token;
        token1= Common.yaml_util.read_Yaml("aaccess_token")##yaml文件读取token值
        heads ={
        "Content-Type ":"application/json",
        "token":token1,
        "Access-Control-Allow-Methods ":"GET, POST, OPTIONS",
        }
        # getResponse = requests.request(method='get',url=url,headers=heads)
        getResponse = TestEduitProject.access_session.request(method='get', url=url, headers=heads)#通过session创建关联的会话
        getResponse_json = getResponse.json()
        data =getResponse_json.get("data")
        project_uuid=data[1].get("project_uuid")
        print(project_uuid)
        # S = getResponse_json.loads();//json格式转换成字典格式
        # D = S.dumps();//字典格式装换成json格式
    @pytest.mark.run(order=1)
    def test_jump(self):
        print("测试")






