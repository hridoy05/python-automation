import re
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def test_phone_number():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://bikroy.com/en/ads/dhaka")
    timeout = 5

    my_elements = driver.find_elements_by_class_name('normal--2QYVk')
    print(my_elements)
    element = my_elements[-1]
    element.click()
    time.sleep(3)
    timeout = 3
    phone_button = driver.find_element_by_class_name('call-button--3uvWj')
    phone_button.click()
    phone_numbers = driver.find_elements_by_class_name('phone-numbers--2COKR')
    # print(len(phone_numbers.gettext()))
    time.sleep(3)
    numList = []
    for i in phone_numbers:
        Pattern = re.compile(r'^(?:\d88|88)?(01[3-9]\d{8})$')
        if Pattern.match(i.text):
            assert True

    # assert my_element.is_displayed()
    driver.quit()
