#!/usr/bin/python
# coding=utf-8
from selenium.webdriver.common.by import By
from base import Base
from selenium import webdriver
import os
import unittest


class WebDemo(unittest.TestCase):
    """ai test """

    @classmethod
    def setUpClass(cls) -> None:
        print(cls.docs)
        driver_path = os.path.join(os.getcwd(), "webdriver", "chromedriver.exe")
        cls.driver = webdriver.Chrome(executable_path=driver_path)
        cls.base = Base(cls.driver)
        cls.base.open_page("http://www.baidu.com")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        print("关闭浏览器")

    def test_case001(self):
        print("this test001")
        self.base.find_element(By.ID, "kw").send_keys("selenium2 python")
        self.base.find_element(By.ID, "su").click()
        print(self.base.get_title())
        pass

    def test_case002(self):
        print("this is test002")
        self.base.open_page("https://www.cnblogs.com/Rita-LJ/p/8079094.html")
        print(self.base.get_title())
        pass


if __name__ == '__main__':
    unittest.main()
