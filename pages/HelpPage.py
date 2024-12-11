from selenium.webdriver import ActionChains

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure

class HelpPageLocators:
    ADVERTISEMENT_CABINET = (By.XPATH, '//a[contains(@href, "reklamnyi-kabinet")]')

class HelpPageHelperHelper(BasePageHelper):
        def __init__(self, driver):
            self.driver = driver
            self.check_page()

        def check_page(self):
            self.find_element(HelpPageLocators.ADVERTISEMENT_CABINET)

        def scrollToitem(self, locator):
            scroll_item = self.find_element(locator)
            ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()


