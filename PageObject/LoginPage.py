from locator import Data
from selenium.webdriver.common.by import By


class Login:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(Data.url)

    def input_login(self):
        self.browser.find_element(By.CSS_SELECTOR, Data.login_field['css']).clear()
        self.browser.find_element(By.CSS_SELECTOR, Data.login_field['css']).send_keys(Data.login)

    def input_password(self):
        self.browser.find_element(By.CSS_SELECTOR, Data.password_field['css']).clear()
        self.browser.find_element(By.CSS_SELECTOR, Data.password_field['css']).send_keys(Data.password)

    def click_login_button(self):
        self.browser.find_element(By.CSS_SELECTOR, Data.button_login['css']).click()
        self.browser.implicitly_wait(20)
