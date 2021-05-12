from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def test_last_add():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://bikroy.com/en/ads/dhaka")
    timeout = 5
    time.sleep(3)
    # my_elements = driver.find_elements_by_class_name('normal--2QYVk')
    # print(my_elements)
    my_elements = WebDriverWait(driver, 10).until(EC.element_located_to_be_selected((By.CLASS_NAME, "normal--2QYVk")))
    print(my_elements)
    # element = my_elements[-1].text
    # element.click()

    # assert my_element.is_displayed()
    driver.quit()
