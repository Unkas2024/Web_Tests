import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class LoginPageLocators:
    Login_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    Login_Field = (By.XPATH, '//*[@id="field_email"]')
    Password_button = (By.XPATH, '//*[@id="field_password"]')
    Login_Button = (By.XPATH, '//*[@data-l="t,sign_in"]')
    Input_QRCode = (By.XPATH, '//*[@class ="qr-button-label"]')
    Not_Input = (By.XPATH, '//*[@class="lp"]')
    Not_Profile = (By.XPATH, '//*[@class="external-oauth-login_title-tx"]')
    Registration_button = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    VK_button = (By.XPATH, '//*[@class="social-icon-button-v2_vkid-text"]')
    Mail_button = (By.XPATH, '//*[@class="h-mod __small __mailru social-icon-button-v2"]')
    Yandex_button = (By.XPATH, '//*[@class= "h-mod __small __yandex social-icon-button-v2"]')
    Google_button = (By.XPATH, '//*[@class= "h-mod social-icon-button-v2 __other_providers"]')

    #   LOGIN_FIELD = (By.ID, 'field_email')
    #   PASSWORD_FIELD = (By.ID, 'field_password')
    #   LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    #   LOGIN_BY_QR_CODE = (By.XPATH, '//*[@data-l="t,get_qr"]')
    #   RESTORE_LINK = (By.XPATH, '//*[@data-l="t,restore"]')
    #   REGISTRATION_BUTTON = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    #    VK_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    #    MAIL_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    #    YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    #    OTHER_BUTTON = (By.XPATH, '//*[@data-l="t,other"]')

    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')
    Restore_link = (By.XPATH, '//*[@data-l="t,restore"]')
    Profile_link = (By.NAME, 'st.go_to_recovery')


class LoginPageHelper(BasePageHelper):
    def __init__(self, driver: object) -> object:
        self.driver = driver
        self.check_page()

    @allure.step('Проверяем корректность загрузки страницы')
    def check_page(self):
        self.find_element(LoginPageLocators.Login_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.Login_Field)
        self.find_element(LoginPageLocators.Password_button)
        self.find_element(LoginPageLocators.Login_Button)
        self.find_element(LoginPageLocators.Input_QRCode)
        self.find_element(LoginPageLocators.Not_Input)
        self.find_element(LoginPageLocators.Not_Profile)
        self.find_element(LoginPageLocators.Registration_button)
        self.find_element(LoginPageLocators.VK_button)
        self.find_element(LoginPageLocators.Mail_button)
        self.find_element(LoginPageLocators.Yandex_button)
        self.find_element(LoginPageLocators.Google_button)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.Login_Button).click()

    @allure.step('Получаем код ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Заполняем поле логин')
    def type_login(self, login):
        self.find_element(LoginPageLocators.Login_Field).send_keys(login)
        self.attach_screenshot()

    @allure.step('Заполняем поле пароль')
    def type_password(self, password):
        self.find_element(LoginPageLocators.Password_button).send_keys(password)
        self.attach_screenshot()

    @allure.step('Перейти к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.Profile_link).click()

    @allure.step('Перейти регистрации')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.Registration_button).click()
