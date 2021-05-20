from selenium.webdriver.common.by import By


class TestData:
    # CHROME_EXECUTABLE_PATH = "C:/Users/LS\Desktop/driver"
    BASE_URL = "https://bikroy.com/en"
    BASE_URL_DHAKA = "https://bikroy.com/en/ads/dhaka"
    BASE_URL_CHATTOGRAM = "https://bikroy.com/en/ads/chattogram"
    BASE_URL_KHULNA = "https://bikroy.com/en/ads/khulna"
    BASE_URL_MYMENSINGH = "https://bikroy.com/en/ads/mymensingh"
    BASE_URL_RAJSHAHI = "https://bikroy.com/en/ads/rajshahi"
    BASE_URL_RANGPUR = "https://bikroy.com/en/ads/rangpur"
    BASE_URL_SYLHET = "https://bikroy.com/en/ads/sylhet"

    """BY locators"""
    LOWEST_AD = 'normal--2QYVk'
    ELEMENT_TEXT = (By.XPATH, '//div[text()="Description"]')
    NUMBER_BUTTON = (By.CLASS_NAME, "call-button--3uvWj")
    VALID_NUMBER = 'phone-numbers--2COKR'