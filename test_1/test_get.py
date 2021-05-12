import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_get():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://bikroy.com/")
    driver.implicitly_wait(5)
    assert driver.title == "Bikroy.com - বাংলাদেশে ইলেকট্রনিকস, গাড়ি, প্রপার্টি এবং চাকরি"
    time.sleep(3)
    driver.quit()
