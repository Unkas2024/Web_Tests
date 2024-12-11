from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure

class CabinetHelpLocators:
    Title = (By.XPATH, '//span[text()="Рекламный кабинет"]')

class CabinetHelp(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(CabinetHelpLocators.Title)

