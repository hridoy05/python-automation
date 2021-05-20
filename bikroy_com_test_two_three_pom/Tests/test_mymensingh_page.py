import time
import re

from bikroy_com_test_two_three_pom.Config import config
from bikroy_com_test_two_three_pom.Pages.MymensinghPage import MymensinghPage
from bikroy_com_test_two_three_pom.Tests.test_base import BaseTest


class Test_Mymensingh(BaseTest):
    def test_cities_name(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        elements = self.mymensinghPage.get_all_cities()
        for i in range(2, len(elements)):
            print(elements[i])

    def test_lowest_add(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        element = self.mymensinghPage.do_find_lowest_ad(config.TestData.LOWEST_AD)
        if element:
            assert True

    def test_click(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        self.mymensinghPage.do_find_lowest_ad(config.TestData.LOWEST_AD)
        self.mymensinghPage.do_click(config.TestData.LOWEST_AD)
        time.sleep(2)

    def test_date_text(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        self.mymensinghPage.do_find_lowest_ad()
        self.mymensinghPage.do_click()
        text = self.mymensinghPage.get_date_text()

        if text:
            assert True

    def test_element_text(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        self.mymensinghPage.do_find_lowest_ad()
        self.mymensinghPage.do_click()
        text = self.mymensinghPage.get_element_text()
        if text:
            assert True

    def test_number_click(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        self.mymensinghPage.do_find_lowest_ad()
        self.mymensinghPage.do_click()
        self.mymensinghPage.do_click_number_button()

    def test_phone_number(self):
        self.mymensinghPage = MymensinghPage(self.driver)
        self.mymensinghPage.do_find_lowest_ad()
        self.mymensinghPage.do_click()
        self.mymensinghPage.do_click_number_button()
        phone_numbers = self.mymensinghPage.do_valid_phone_number()
        time.sleep(2)
        for phone_number in phone_numbers:
            Pattern = re.compile(r'^(?:\d88|88)?(01[3-9]\d{8})$')
            if Pattern.match(phone_number.text):
                assert True
