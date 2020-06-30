#!/usr/bin/python3
# coding=utf-8


class Base(object):
    def __init__(self, driver):
        driver.implicitly_wait(time_to_wait=20)
        driver.maximize_window()
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open_page(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.current_url
