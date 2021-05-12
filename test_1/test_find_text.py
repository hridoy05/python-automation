from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_find_text():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://bikroy.com/")
    driver.implicitly_wait(5)
    my_element = driver.find_element_by_xpath("//div[text()='Copyright © Saltside Technologies']").is_displayed()
    # print(my_element)
    # text = "Copyright © Saltside Technologies"
    assert my_element
    driver.quit()
