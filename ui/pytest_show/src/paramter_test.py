import unittest
from parameterized import (
    parameterized, parameterized_class)


class TestParam(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass
    @classmethod
    def  tearDownClass(cls) -> None:
        pass

    @parameterized.expand([(2,3,5),(1,2,3)])
    def test_01(self,a,b,exp):
        print("a+b is {} ,exp is {}".format(a+b,exp))
        self.assertEqual(a+b,exp)


@parameterized_class(('a', 'b', 'exp'), [
   (1, 2, 3),
   (5, 5, 10),
])
class ParamClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_run(self):
        pass
        print("c +d is {} ,exp is {}".format(self.a+self.b,self.exp))
        self.assertEqual(self.a+self.b,self.exp)

if __name__ == '__main__':
    unittest.main(verbosity=2)