import allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelperHelper, HelpPageLocators
from pages.Cabinet import CabinetHelp


Base_URL = 'https://ok.ru/help'

def test_help_test(browser):
    BasePageHelper(browser).get_url(Base_URL)
    HelpPage = HelpPageHelperHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISEMENT_CABINET)
    CabinetHelp(browser)



