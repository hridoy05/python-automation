import time
import re

from bikroy_com_test_two_three_pom.Config import config
from bikroy_com_test_two_three_pom.Pages.DhakaPage import DhakaPage
from bikroy_com_test_two_three_pom.Tests.test_base import BaseTest


class Test_Dhaka(BaseTest):

    def test_cities_name(self):
        self.dhakaPage = DhakaPage(self.driver)
        elements = self.dhakaPage.get_all_cities()
        for i in range(2, len(elements)):
            print(elements[i])

    def test_lowest_add(self):
        self.dhakaPage = DhakaPage(self.driver)
        element = self.dhakaPage.do_find_lowest_ad()
        if element:
            assert True

    def test_click(self):
        self.dhakaPage = DhakaPage(self.driver)
        self.dhakaPage.do_find_lowest_ad()
        self.dhakaPage.do_click()
        time.sleep(2)

    def test_date_text(self):
        self.dhakaPage = DhakaPage(self.driver)
        self.dhakaPage.do_find_lowest_ad()
        self.dhakaPage.do_click()
        text = self.dhakaPage.get_date_text()
        print(text)
        if text:
            assert True

    def test_element_text(self):
        self.dhakaPage = DhakaPage(self.driver)
        self.dhakaPage.do_find_lowest_ad()
        self.dhakaPage.do_click()
        text = self.dhakaPage.get_element_text()
        if text:
            assert True

    def test_number_click(self):
        self.dhakaPage = DhakaPage(self.driver)
        self.dhakaPage.do_find_lowest_ad()
        self.dhakaPage.do_click()
        self.dhakaPage.do_click_number_button()

    def test_phone_number(self):
        self.dhakaPage = DhakaPage(self.driver)
        self.dhakaPage.do_find_lowest_ad()
        self.dhakaPage.do_click()
        self.dhakaPage.do_click_number_button()
        phone_numbers = self.dhakaPage.do_valid_phone_number()
        time.sleep(2)
        for phone_number in phone_numbers:
            Pattern = re.compile(r'^(?:\d88|88)?(01[3-9]\d{8})$')
            if Pattern.match(phone_number.text):
                assert True
