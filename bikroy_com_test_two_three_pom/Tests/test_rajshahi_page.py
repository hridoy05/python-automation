import time
import re
import pytest

from bikroy_com_test_two_three_pom.Pages.RajshahiPage import RajshahiPage
from bikroy_com_test_two_three_pom.Tests.test_base import BaseTest


class Test_Rajshahi(BaseTest):

    def test_cities_name(self):
        self.rajshahiPage = RajshahiPage(self.driver)
        elements = self.rajshahiPage.name_all_cities()
        for i in range(2, len(elements)):
            print(elements[i])

    def test_lowest_add(self):
        self.rajshahiPage = RajshahiPage(self.driver)
        element = self.rajshahiPage.get_lowest_add()
        if element:
            assert True

    def test_click(self):
        self.rajshahiPage = RajshahiPage(self.driver)
        self.rajshahiPage.click()
        time.sleep(3)

    def test_date_text(self):
        self.rajshahiPage = RajshahiPage(self.driver)
        text = self.rajshahiPage.date_text()
        if text:
            assert True

    def test_element_text(self):
        self.rajshahiPage = RajshahiPage(self.driver)
        text = self.rajshahiPage.element_text()
        if text:
            assert True

    def test_number_click(self):
        self.rajshahiPage = RajshahiPage(self.driver)
        self.rajshahiPage.click_number_button()
        time.sleep(3)

    def test_phone_number(self):
        self.rajshahiPage = RajshahiPage(self.driver)
        phone_numbers = self.rajshahiPage.valid_phone_number()
        time.sleep(3)
        numList = []
        for phone_number in phone_numbers:
            Pattern = re.compile(r'^(?:\d88|88)?(01[3-9]\d{8})$')
            if Pattern.match(phone_number.text):
                assert True
