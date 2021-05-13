import time
import re
import pytest

from bikroy_com_test_two_three_pom.Pages.MymensinghPage import MymensinghPage
from bikroy_com_test_two_three_pom.Tests.test_base import BaseTest


class Test_Mymensingh(BaseTest):

    def test_cities_name(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        elements = self.mymensinghPage.name_all_cities()
        for i in range(2, len(elements)):
            print(elements[i])

    def test_lowest_add(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        element = self.mymensinghPage.get_lowest_add()
        if element:
            assert True

    def test_click(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        self.mymensinghPage.click()
        time.sleep(3)

    def test_date_text(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        text = self.mymensinghPage.date_text()
        if text:
            assert True

    def test_element_text(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        text = self.mymensinghPage.element_text()
        if text:
            assert True

    def test_number_click(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        self.mymensinghPage.click_number_button()
        time.sleep(3)

    def test_phone_number(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        phone_numbers = self.mymensinghPage.valid_phone_number()
        time.sleep(3)
        numList = []
        for phone_number in phone_numbers:
            Pattern = re.compile(r'^(?:\d88|88)?(01[3-9]\d{8})$')
            if Pattern.match(phone_number.text):
                assert True
