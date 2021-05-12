# By.CLASS_NAME, "sub-title--37mkY"
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def test_last_add():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://bikroy.com/en/ads/dhaka")
    timeout = 5
    time.sleep(3)
    my_elements = driver.find_elements_by_class_name('normal--2QYVk')
    element = my_elements[-1]
    print(element.click())
    text = driver.execute_script("return document.getElementsByClassName('sub-title--37mkY')[0].innerText;")
    print(text)

    if text:
        assert True






    # my_elements = driver.find_elements_by_class_name('normal--2QYVk')
    # element = my_elements[-1]
    # print(element.click())
    # my_element = driver.find_elements_by_class_name('sub-title--37mkY')
    # print(len(my_element))
    # print(my_element.get_attribute('innerHTML'))
    # # if element:
    #     assert True

    # assert my_element.is_displayed()
    driver.quit()
