import allure
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import random

class RegistrPageLocators:
    Phone_Field = (By.XPATH, '//div[@data-l="t,phone"]')
    Country_List = (By.XPATH, '//div[@data-l="t,country"]')
    Country_Item = (By.XPATH, '//*[@class="country-select_i"]')
    Submit_Button = (By.XPATH, '//input[@data-l="t,submit"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-l="t,support"]')


class RegistrationPageHelperHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.find_element(RegistrPageLocators.Phone_Field)
            self.find_element(RegistrPageLocators.Country_List)
            self.find_element(RegistrPageLocators.Submit_Button)
            self.find_element(RegistrPageLocators.SUPPORT_BUTTON)
#            self.find_element(RegistrPageLocators.Country_Item)

    def select_random_country(self):
        random_number = random.randint(0, 212)
        self.find_element(RegistrPageLocators.Country_List).click()
        country_items = self.find_elements(RegistrPageLocators.Country_Item)
        country_code = country_items[random_number].text
        country_items[random_number].click()



    def get_phone_field_value(self):
        return self.find_element(RegistrPageLocators.Phone_Field).get_attribute('value')

