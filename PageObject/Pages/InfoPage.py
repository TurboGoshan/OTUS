from locator import Data
from selenium.webdriver.common.by import By


class Info:

    def __init__(self, browser):
        self.browser = browser

    def check_page(self):
        update_text = self.browser.find_element(By.CSS_SELECTOR, Data.button_update['css'])
        assert update_text != True

    def check_title(self):
        title_name = self.browser.find_element(By.ID, Data.user_title['id'])
        assert title_name.text == 'John Smith (test)'

    def check_name(self):
        check_name = self.browser.find_element(By.XPATH, Data.name_field['xpath'])
        value = check_name.get_attribute('value')
        assert value == 'John Smith'
