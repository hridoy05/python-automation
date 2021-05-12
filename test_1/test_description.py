from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def test_description():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://bikroy.com/en/ads/dhaka")
    timeout = 5
    time.sleep(3)
    my_elements = driver.find_elements_by_class_name('normal--2QYVk')
    element = my_elements[-1]
    element.click()
    time.sleep(2)
    des = driver.find_element(By.XPATH, '//div[text()="Description"]')
    time.sleep(2)
    print(des.text)

    # assert my_element.is_displayed()
    driver.quit()
