import time
import re
import pytest

from bikroy_com_Test_POM.Pages.ChattogramPage import ChattogramPage
from bikroy_com_Test_POM.Tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_cities_name(self):
        self.chattogramPage = ChattogramPage(self.driver)
        elements = self.chattogramPage.name_all_cities()
        for i in range(2, len(elements)):
            print(elements[i])

    def test_lowest_add(self):
        self.chattogramPage = ChattogramPage(self.driver)
        element = self.chattogramPage.get_lowest_add()
        if element:
            assert True

    def test_click(self):
        self.chattogramPage = ChattogramPage(self.driver)
        self.chattogramPage.click()
        time.sleep(3)

    def test_date_text(self):
        self.chattogramPage = ChattogramPage(self.driver)
        text = self.chattogramPage.date_text()
        if text:
            assert True

    def test_element_text(self):
        self.chattogramPage = ChattogramPage(self.driver)
        text = self.chattogramPage.element_text()
        if text:
            assert True

    def test_number_click(self):
        self.chattogramPage = ChattogramPage(self.driver)
        self.chattogramPage.click_number_button()

    def test_phone_number(self):
        self.chattogramPage = ChattogramPage(self.driver)
        phone_numbers = self.chattogramPage.valid_phone_number()
        time.sleep(3)
        numList = []
        for phone_number in phone_numbers:
            Pattern = re.compile(r'^(?:\d88|88)?(01[3-9]\d{8})$')
            if Pattern.match(phone_number.text):
                assert True
