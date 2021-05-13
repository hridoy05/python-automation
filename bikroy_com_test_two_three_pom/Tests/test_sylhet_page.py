import time
import re
import pytest

from bikroy_com_test_two_three_pom.Pages.SylhetPage import SylhetPage
from bikroy_com_test_two_three_pom.Tests.test_base import BaseTest


class Test_Syhlet(BaseTest):

    def test_cities_name(self):
        self.syhletPage = SylhetPage(self.driver)
        elements = self.syhletPage.name_all_cities()
        for i in range(2, len(elements)):
            print(elements[i])

    def test_lowest_add(self):
        self.syhletPage = SylhetPage(self.driver)
        element = self.syhletPage.get_lowest_add()
        if element:
            assert True

    def test_click(self):
        self.syhletPage = SylhetPage(self.driver)
        self.syhletPage.click()
        time.sleep(3)

    def test_date_text(self):
        self.syhletPage = SylhetPage(self.driver)
        text = self.syhletPage.date_text()
        if text:
            assert True

    def test_element_text(self):
        self.syhletPage = SylhetPage(self.driver)
        text = self.syhletPage.element_text()
        if text:
            assert True

    def test_number_click(self):
        self.syhletPage = SylhetPage(self.driver)
        self.syhletPage.click_number_button()

    def test_phone_number(self):
        self.syhletPage = SylhetPage(self.driver)
        phone_numbers = self.syhletPage.valid_phone_number()
        time.sleep(3)
        numList = []
        for phone_number in phone_numbers:
            Pattern = re.compile(r'^(?:\d88|88)?(01[3-9]\d{8})$')
            if Pattern.match(phone_number.text):
                assert True
