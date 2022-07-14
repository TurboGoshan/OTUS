from locator import Page
from selenium.webdriver.common.by import By
from selenium import webdriver


def test_header(browser):
    browser.get(Page.URL)
    browser.implicitly_wait(20)
    header_exists = browser.find_element(By.CSS_SELECTOR, Page.Header_CSS)
    assert header_exists != True


def test_items(browser):
    browser.get(Page.URL)
    browser.implicitly_wait(20)
    browser.find_element(By.LINK_TEXT, Page.Item_text_1).click()
    browser.implicitly_wait(20)
    browser.find_element(By.LINK_TEXT, Page.Item_text_2).click()
    browser.implicitly_wait(20)
    browser.find_element(By.LINK_TEXT, Page.Item_text_3).click()
    browser.implicitly_wait(20)
    browser.find_element(By.LINK_TEXT, Page.Item_text_4).click()
    browser.implicitly_wait(20)
    browser.find_element(By.LINK_TEXT, Page.Item_text_5).click()
    browser.implicitly_wait(20)
    element1 = browser.find_element(By.LINK_TEXT, Page.Item_text_6)
    browser.execute_script("arguments[0].click();", element1)
    browser.implicitly_wait(20)
    element2 = browser.find_element(By.LINK_TEXT, Page.Item_text_7)
    browser.execute_script("arguments[0].click();", element2)


def test_login(browser):
    browser.get(Page.URL)
    browser.implicitly_wait(20)
    browser.find_element(By.CSS_SELECTOR, Page.Search_feld_CSS).send_keys("test")
    browser.find_element(By.CSS_SELECTOR, Page.Search_feld_CSS).submit()
    browser.implicitly_wait(20)
    x = browser.find_element(By.CSS_SELECTOR, "a[class='ks-active ks-non-clickable']")
    assert x != True


def test_attribute():
    browser1 = webdriver.Chrome()
    browser1.get(Page.URL)
    x = browser1.find_element(By.CSS_SELECTOR, "a[class='submenu-lvl1__link']")
    y = x.get_attribute('href')
    assert y == "https://www.1a.lv/c/datortehnika-preces-birojam/2pd"
