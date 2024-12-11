import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VKEcosystemPage import VKEcosystemPageHelper


Base_URL = 'https://ok.ru/'

allure.suite('Проверка тулбара')
allure.title('Переход к проектам экосистемы VK')
def test_open_vk_ecosystem(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(Base_URL)
    BasePage.check_page()
    LoginPage = LoginPageHelper(browser)
    current_windows_id = LoginPage.get_windows_id(0)
    LoginPage.click_vk_ecosystem()
    LoginPage.click_more_button()
    new_window_id = LoginPage.get_windows_id(1)
    LoginPage.switch_window(new_window_id)
    VKEcosystemPage = VKEcosystemPageHelper(browser)
    VKEcosystemPage.switch_window(current_windows_id)
    LoginPageHelper(browser)

#    current_windows_id = LoginPage.get_windows_id(0)
#    LoginPage.click_vk_ecosystem()
#    LoginPage.click_more_button()
#    new_window_id = LoginPage.get_windows_id (1)
#    LoginPage.switch.window(new_window_id)
#
#    VKEcosysytemPage.switch_window(current_windows_id)
#    LoginPageHelperHelper(browser)




