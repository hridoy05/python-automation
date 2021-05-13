import time
import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Footer(BaseTest):
    def get_page(self):
        self.driver.get("https://bikroy.com/en/ads")
        self.driver.implicitly_wait(10)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def test_go_to(self):
        self.driver.get("https://bikroy.com/en/ads")

    def test_scroll_down(self):
        self.get_page()

    def test_text(self):
        self.get_page()
        my_element = self.driver.find_element_by_xpath(
            "//div[text()='Copyright © Saltside Technologies']").is_displayed()
        assert my_element

    """More from Bikroy"""

    def test_sell_first_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Sell Fast").click()

    def test_doorstep_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Doorstep Delivery").click()

    def test_membership_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Membership").click()

    def test_banner_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Banner Ads").click()

    def test_promotions_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Promotions").click()

    def test_staffing_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Staffing solutions").click()

    """Help&Support"""

    def test_faq_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("FAQ").click()

    def test_stay_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Stay safe").click()

    def test_contact_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Contact Us").click()

    """Follw Bikroy"""

    def test_blog_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Blog").click()

    def test_facebook_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Facebook").click()

    def test_twitter_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Twitter").click()

    def test_youtube_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Youtube").click()

    """About Bikroy"""

    def test_about_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("About Us").click()

    def test_careers_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Careers").click()

    def test_terms_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Terms and Conditions").click()

    def privacy_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Privacy policy").click()

    def test_sitemap_link(self):
        self.get_page()
        self.driver.find_element_by_link_text("Sitemap").click()
