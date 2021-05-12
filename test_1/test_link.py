from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_link():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://bikroy.com/en/ads")
    driver.implicitly_wait(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element_by_link_text("Sell Fast").click()
    time.sleep(3)
    driver.quit()
