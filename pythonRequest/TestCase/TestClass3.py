import pytest
@pytest.fixture(scope='function',params=['成龙','甄子丹','才'])
def my_fixtrue(request):
    print('前置')
    yield request.param
    print('后置')
class TestMashang1:
    def test_01_babby(self):
        print('test1')
    def test_02_baby(self,my_fixtrue):
        print('test2')
        print('----'+str(my_fixtrue))

