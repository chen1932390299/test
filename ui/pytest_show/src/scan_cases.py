# coding=utf-8
import inspect
import unittest
from demo import GetParams
from HTMLReport import logger
import jsonpath
import json
from requests import session
class ApiFrame(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger=logger()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

def run_test(self,case_name,req):

    testFunc = getattr(ApiFrame,case_name)
    #print("testFnc is : ",testFunc)  #lambda
    response=req.api_request(case_name)  # loads str ->dict
    print(response)
    # assert_msg=jsonpath.jsonpath(json.loads(response),"$..password")[0]
    # print(assert_msg)
    # assert  assert_msg =="testapi"

if __name__ == '__main__':

    app=ApiFrame()
    r=GetParams(sessions=session())
    print("r is ",r.sessions)
    setattr(ApiFrame,"test_case001",lambda self:run_test(self,"test_case001",r))
    # app.test_case001("test_case001")
    setattr(ApiFrame,"test_case002",lambda self:run_test(self,"test_case002",r))
    suite = unittest.TestLoader().loadTestsFromTestCase(ApiFrame)
    print(suite)
    unittest.TextTestRunner().run(suite)


