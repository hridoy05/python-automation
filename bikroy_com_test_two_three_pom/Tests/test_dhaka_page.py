import time
import re
import pytest

from bikroy_com_test_two_three_pom.Pages.DhakaPage import DhakaPage
from bikroy_com_test_two_three_pom.Tests.test_base import BaseTest


class Test_Dhaka(BaseTest):

    def test_cities_name(self):
        self.dhakaPage = DhakaPage(self.driver)
        elements = self.dhakaPage.name_all_cities()
        for i in range(2, len(elements)):
            print(elements[i])

    def test_lowest_add(self):
        self.dhakaPage = DhakaPage(self.driver)
        element = self.dhakaPage.get_lowest_add()
        if element:
            assert True

    def test_click(self):
        self.dhakaPage = DhakaPage(self.driver)
        self.dhakaPage.click()
        time.sleep(3)

    def test_date_text(self):
        self.dhakaPage = DhakaPage(self.driver)
        text = self.dhakaPage.date_text()
        if text:
            assert True

    def test_element_text(self):
        self.dhakaPage = DhakaPage(self.driver)
        text = self.dhakaPage.element_text()
        if text:
            assert True

    def test_number_click(self):
        self.dhakaPage = DhakaPage(self.driver)
        self.dhakaPage.click_number_button()

    def test_phone_number(self):
        self.dhakaPage = DhakaPage(self.driver)
        phone_numbers = self.dhakaPage.valid_phone_number()
        time.sleep(3)
        numList = []
        for phone_number in phone_numbers:
            Pattern = re.compile(r'^(?:\d88|88)?(01[3-9]\d{8})$')
            if Pattern.match(phone_number.text):
                assert True
