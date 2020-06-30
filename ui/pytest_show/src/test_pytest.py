import  pytest

mobile_list = ['10010', '10086']
code_list = ['x2zx', 'we2a']


@pytest.mark.parametrize('phone,code',zip(mobile_list,code_list))
def test_001(phone,code):
    print("phone is {} ,code is {}".format(phone,code))
@pytest.mark.chensmoke
def test_002():
    print("this is test smoke...")

if __name__ == '__main__':
    pytest.main(["./test_pytest.py","-v","-s","-m=chensmoke"])