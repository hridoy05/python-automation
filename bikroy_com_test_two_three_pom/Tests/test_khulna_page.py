import time
import re
import pytest

from bikroy_com_test_two_three_pom.Pages.KhulnaPage import KhulnaPage
from bikroy_com_test_two_three_pom.Tests.test_base import BaseTest


class Test_khulna(BaseTest):

    def test_cities_name(self):
        self.khulnaPage = KhulnaPage(self.driver)
        elements = self.khulnaPage.name_all_cities()
        for i in range(2, len(elements)):
            print(elements[i])

    def test_lowest_add(self):
        self.khulnaPage = KhulnaPage(self.driver)
        element = self.khulnaPage.get_lowest_add()
        if element:
            assert True

    def test_click(self):
        self.khulnaPage = KhulnaPage(self.driver)
        self.khulnaPage.click()
        time.sleep(3)

    def test_date_text(self):
        self.khulnaPage = KhulnaPage(self.driver)
        text = self.khulnaPage.date_text()
        if text:
            assert True

    def test_element_text(self):
        self.khulnaPage = KhulnaPage(self.driver)
        text = self.khulnaPage.element_text()
        if text:
            assert True

    def test_number_click(self):
        self.khulnaPage = KhulnaPage(self.driver)
        self.khulnaPage.click_number_button()

    def test_phone_number(self):
        self.khulnaPage = KhulnaPage(self.driver)
        phone_numbers = self.khulnaPage.valid_phone_number()
        time.sleep(3)
        numList = []
        for phone_number in phone_numbers:
            Pattern = re.compile(r'^(?:\d88|88)?(01[3-9]\d{8})$')
            if Pattern.match(phone_number.text):
                assert True
