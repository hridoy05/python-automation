from bikroy_com_test_two_three_pom.Config import config
from bikroy_com_test_two_three_pom.Pages.BasePage import BasePage


class ChattogramPage(BasePage):
    """constructors of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(config.TestData.BASE_URL_CHATTOGRAM)
