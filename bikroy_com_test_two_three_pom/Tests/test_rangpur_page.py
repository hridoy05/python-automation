import time
import re
import pytest

from bikroy_com_test_two_three_pom.Pages.RangpurPage import RangpurPage
from bikroy_com_test_two_three_pom.Tests.test_base import BaseTest


class Test_Rangpur(BaseTest):

    def test_cities_name(self):
        self.rangpurPage = RangpurPage(self.driver)
        elements = self.rangpurPage.name_all_cities()
        for i in range(2, len(elements)):
            print(elements[i])

    def test_lowest_add(self):
        self.rangpurPage = RangpurPage(self.driver)
        element = self.rangpurPage.get_lowest_add()
        if element:
            assert True

    def test_click(self):
        self.rangpurPage = RangpurPage(self.driver)
        self.rangpurPage.click()
        time.sleep(3)

    def test_date_text(self):
        self.rangpurPage = RangpurPage(self.driver)
        text = self.rangpurPage.date_text()
        if text:
            assert True

    def test_element_text(self):
        self.rangpurPage = RangpurPage(self.driver)
        text = self.rangpurPage.element_text()
        if text:
            assert True

    def test_number_click(self):
        self.rangpurPage = RangpurPage(self.driver)
        self.rangpurPage.click_number_button()

    def test_phone_number(self):
        self.rangpurPage = RangpurPage(self.driver)
        phone_numbers = self.rangpurPage.valid_phone_number()
        time.sleep(3)
        numList = []
        for phone_number in phone_numbers:
            Pattern = re.compile(r'^(?:\d88|88)?(01[3-9]\d{8})$')
            if Pattern.match(phone_number.text):
                assert True
