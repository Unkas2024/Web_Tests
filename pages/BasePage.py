import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO_Button = (By.ID, 'nohook_logo_link')
    VK_Ecosystem_button = (By.XPATH, '//*[@data-l="t,vk_ecosystem"]')
    More_button = (By.XPATH, '//*[@data-l="t,more"]')


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver


    def check_page(self):
        self.find_element(BasePageLocators.LOGO_Button)
        self.find_element(BasePageLocators.VK_Ecosystem_button)


    def find_element(self, locator: object, time: object = 5) -> object:
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator),
                                                      message=f"Не удалось найти элемент {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator),
                                                      message=f"Не удалось найти элементы {locator}")

    @allure.step('Открываем главную страницу')
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)

    @allure.step('Открываем кнопку экосистемы')
    def click_vk_ecosystem(self):
        self.find_element(BasePageLocators.VK_Ecosystem_button).click()

    @allure.step('Открываем кнопку экосистемы')
    def click_more_button(self):
        self.find_element(BasePageLocators.More_button).click()

    def get_windows_id(self, index):
        return self.driver.window_handles[index]

    def switch_window(self, window_id):
        self.driver.switch_to.window(window_id)
