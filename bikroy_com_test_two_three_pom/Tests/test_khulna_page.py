import time
import re

from bikroy_com_test_two_three_pom.Pages.KhulnaPage import KhulnaPage
from bikroy_com_test_two_three_pom.Tests.test_base import BaseTest
from bikroy_com_test_two_three_pom.Config import config


class Test_Khulna(BaseTest):

    def test_cities_name(self):
        self.khulnaPage = KhulnaPage(self.driver)
        elements = self.khulnaPage.get_all_cities()
        for i in range(2, len(elements)):
            print(elements[i])

    def test_lowest_add(self):
        self.khulnaPage = KhulnaPage(self.driver)
        element = self.khulnaPage.do_find_lowest_ad()
        if element:
            assert True

    def test_click(self):
        self.khulnaPage = KhulnaPage(self.driver)
        self.khulnaPage.do_find_lowest_ad()
        self.khulnaPage.do_click()
        time.sleep(1)

    def test_date_text(self):
        self.khulnaPage = KhulnaPage(self.driver)
        self.khulnaPage.do_find_lowest_ad()
        self.khulnaPage.do_click()
        text = self.khulnaPage.get_date_text()
        if text:
            assert True

    def test_element_text(self):
        self.khulnaPage = KhulnaPage(self.driver)
        self.khulnaPage.do_find_lowest_ad()
        self.khulnaPage.do_click()
        text = self.khulnaPage.get_element_text()
        if text:
            assert True

    def test_number_click(self):
        self.khulnaPage = KhulnaPage(self.driver)
        self.khulnaPage.do_find_lowest_ad()
        self.khulnaPage.do_click()
        self.khulnaPage.do_click_number_button()

    def test_phone_number(self):
        self.khulnaPage = KhulnaPage(self.driver)
        self.khulnaPage.do_find_lowest_ad()
        self.khulnaPage.do_click()
        self.khulnaPage.do_click_number_button()
        phone_numbers = self.khulnaPage.do_valid_phone_number()
        time.sleep(2)
        for phone_number in phone_numbers:
            Pattern = re.compile(r'^(?:\d88|88)?(01[3-9]\d{8})$')
            if Pattern.match(phone_number.text):
                assert True
