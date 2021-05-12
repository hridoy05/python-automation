from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_scroll_up():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://bikroy.com/")
    timeout = 5
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    driver.quit()
