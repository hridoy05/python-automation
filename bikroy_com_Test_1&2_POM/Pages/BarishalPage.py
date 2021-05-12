import pytest
from selenium.webdriver.common.by import By

from bikroy_com_Test_POM.Config import config
from bikroy_com_Test_POM.Pages.BasePage import BasePage


class DhakaPage(BasePage):
    """BY locators"""
    LOWEST_AD = (By.CLASS_NAME, "normal--2QYVk")
    DATE_TEXT = (By.CLASS_NAME, "sub-title--37mkY")
    ELEMENT_TEXT = (By.XPATH, '//div[text()="Description"]')
    NUMBER_BUTTON = (By.CLASS_NAME, "call-button--3uvWj")
    VALID_NUMBER = (By.CLASS_NAME, "phone-numbers--2COKR")

    """constructors of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(config.TestData.BASE_URL_DHAKA)

    """Page actions for dhaka page"""

    """this is used to get name of cities"""

    def name_all_cities(self):
        return self.get_all_cities()

    """this is used to get lowest value"""

    def get_lowest_add(self):
        return self.do_find_lowest_ad(self.LOWEST_AD)

    """this is used to click lowest value"""

    def click(self):
        self.do_click(self.LOWEST_AD)

    """this is used to get text of date"""

    def date_text(self):
        self.do_click(self.LOWEST_AD)
        return self.get_date_text()

    """this is used to get description text"""

    def element_text(self):
        self.do_click(self.LOWEST_AD)
        return self.get_element_text(self.ELEMENT_TEXT)

    """this is used to get number button"""

    def click_number_button(self):
        self.do_click(self.LOWEST_AD)
        self.do_click_number_button(self.NUMBER_BUTTON)

    """this is used to valid phone number"""

    def valid_phone_number(self):
        self.do_click(self.LOWEST_AD)
        return self.do_valid_phone_number()
