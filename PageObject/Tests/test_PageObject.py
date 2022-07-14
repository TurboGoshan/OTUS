from Pages.LoginPage import Login
from Pages.InfoPage import Info


def test_title(browser):
    admin_page = Login(browser)
    admin_page.open()
    admin_page.input_login()
    admin_page.input_password()
    admin_page.click_login_button()
    info_page = Info(browser)
    info_page.check_page()
    info_page.check_title()


def test_name(browser):
    admin_page = Login(browser)
    admin_page.open()
    admin_page.input_login()
    admin_page.input_password()
    admin_page.click_login_button()
    info_page = Info(browser)
    info_page.check_page()
    info_page.check_name()
