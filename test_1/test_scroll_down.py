from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_scroll_down():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://bikroy.com/")
    driver.implicitly_wait(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.quit()
