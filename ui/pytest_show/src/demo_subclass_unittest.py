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
        xx=session()

        cls.rs=GetParams()
        cls.rs.sessions=xx
        print(cls.rs.sessions)

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def assert_anywhere(self,data:dict,json_path:str,expect):
        substitute=jsonpath.jsonpath(data,json_path)

        def cmp_three_way(x,y):
            """@:return:  -1 if x < y,  0 if x == y and   1 if x > y"""
            return (x>y)-(x<y)
        assert cmp_three_way(substitute,expect)==0

    def test_case001(self):
        """ test post method json body """
        module = inspect.stack()[0][3]
        response = self.rs.api_request(module)
        print(response, end="\n")

    def test_case002(self):
        """ test post method with form-data"""
        module = inspect.stack()[0][3]
        response = self.rs.api_request(module)
        print(response, end="\n")

    def test_case003(self):
        """test get method with params"""
        module = inspect.stack()[0][3]
        response = self.rs.api_request(module)
        print(response, end="\n")

    def test_case004(self):
        """test get method no params"""
        module = inspect.stack()[0][3]
        response = self.rs.api_request(module)
        print(response, end="\n")


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(ApiFrame)
    print(suite)
    unittest.TextTestRunner().run(suite)


