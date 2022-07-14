from locator import Data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Login:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.maximize_window()
        self.browser.get(Data.url)
        self.browser.implicitly_wait(20)

    def input_login(self):
        self.browser.find_element(By.CSS_SELECTOR, Data.login_field['css']).clear()
        self.browser.find_element(By.CSS_SELECTOR, Data.login_field['css']).send_keys(Data.login)

    def input_password(self):
        self.browser.find_element(By.CSS_SELECTOR, Data.password_field['css']).clear()
        self.browser.find_element(By.CSS_SELECTOR, Data.password_field['css']).send_keys(Data.password)

    def input_invalid_pass(self):
        self.browser.find_element(By.CSS_SELECTOR, Data.password_field['css']).clear()
        self.browser.find_element(By.CSS_SELECTOR, Data.password_field['css']).send_keys(Data.invalid_password)

    def click_login_button(self):
        self.browser.find_element(By.CSS_SELECTOR, Data.button_login['css']).click()
        self.browser.implicitly_wait(20)
