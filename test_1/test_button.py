from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def test_button():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://bikroy.com/")
    timeout = 5
    time.sleep(3)
    my_element = driver.find_element_by_xpath("//span[text()='POST YOUR AD']")

    assert my_element.is_displayed()
    driver.quit()
