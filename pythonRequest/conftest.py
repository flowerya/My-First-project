#fixtrue，用于部分用例执行之前和执行之后的数据操作
import pytest
import Common.yaml_util

@pytest.fixture(scope='function')
# @pytest.fixture(scope=,params=,autouse=,ids=,name=)
#scope:作用域:class,function,module,package/session,
#params:参数化的信息（list，tumpe，字典）
#autouse：是否要自动化执行



def ex_sql():
    print("用例执行之前")
    yield
    print("测试用例执行之后")
##在所有接口请求之前进行yaml的数据清空(会话级别，然后是自动执行
@pytest.fixture(scope='session',autouse=True)
def cleanYaml():
    Common.yaml_util.clean_Yaml()


