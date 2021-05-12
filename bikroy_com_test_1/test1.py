import pytest
import time


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Bikroy(BaseTest):
    def test_get(self):
        self.driver.get("https://bikroy.com/en")

    def test_scroll_down(self):
        self.driver.get("https://bikroy.com/en")
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

    def test_find_text(self):
        self.driver.get("https://bikroy.com/en")
        my_element = self.driver.find_element_by_xpath("//div[text()='Copyright © Saltside Technologies']")

    def test_text_assert(self):
        self.driver.get("https://bikroy.com/en")
        my_element = self.driver.find_element_by_class_name('copyright')
        assert my_element.text == "Copyright © Saltside Technologies"

    def test_scroll_up(self):
        self.driver.get("https://bikroy.com/en")
        self.driver.execute_script("window.scrollTo(0,0)")

    def test_find_button_text(self):
        self.driver.get("https://bikroy.com/en")
        self.driver.find_element_by_xpath("//span[text()='POST YOUR AD']")

    def test_test_button(self):
        self.driver.get("https://bikroy.com/en")
        my_element = self.driver.find_element_by_xpath("/html/body/nav/div/ul[3]/li[5]/a/span")
        assert my_element.text == "POST YOUR AD"
