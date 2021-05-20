from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from bikroy_com_test_two_three_pom.Config import config

"""This class is the parent of all pages"""
"""It contains all the generic methods and utilities dor all the pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_all_cities(self):
        self.driver.get(config.TestData.BASE_URL)
        timeout = 5
        text = self.driver.execute_script("return document.getElementsByClassName('is-city')[0].innerText;")
        cities = text.split('\n')
        return cities

    def do_find_lowest_ad(self):
        elements = self.driver.find_elements_by_class_name(config.TestData.LOWEST_AD)
        print(list(elements))
        element = elements[-1]
        return element

    def do_click(self):
        elements = self.driver.find_elements_by_class_name(config.TestData.LOWEST_AD)
        print(list(elements))
        element = elements[-1]
        return element.click()

    def get_date_text(self):
        text = self.driver.execute_script("return document.getElementsByClassName('sub-title--37mkY')[0].innerText;")
        return text

    def get_element_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(config.TestData.ELEMENT_TEXT))
        return element.text

    def do_click_number_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(config.TestData.NUMBER_BUTTON)).click()

    def do_valid_phone_number(self):
        element = self.driver.find_elements_by_class_name(config.TestData.VALID_NUMBER)
        print("from base page", element)
        return element
