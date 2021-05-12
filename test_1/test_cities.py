from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def test_button():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://bikroy.com/en")
    # timeout = 5
    # time.sleep(3)
    # cities = driver.find_element(By.CLASS_NAME, "locations-1")
    # print(cities.text)
    text = driver.execute_script("return document.getElementsByClassName('is-city')[0].innerText;")

    timeout = 5
    cities = text.split('\n')
    for i in range(2, len(cities)):
        print(cities[i])
    driver.quit()
