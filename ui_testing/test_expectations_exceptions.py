from selenium.webdriver.support import expected_conditions as ES  # Импортируем явные ожидания
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By  # Для красивого поиска элементов
from locator import Page  # Импорт страниц и адресов элементов из другого файла
import time  # Для задержки времени, для удобного написание тестов


# Проверка переключения страниц с использованием ожидания
def test_pagination(browser):
    # Открывем нужный сайт
    browser.get(Page.url6)
    browser.implicitly_wait(10)
    # Находим текст на первой странице
    text_1 = browser.find_element(By.XPATH, '//*[@id="demo1"]/div[1]/ul/li[1]')
    # Находим номер второй страницы и переключаемся на нее
    page_2 = browser.find_element(By.XPATH, '//*[@id="demo1"]/div[2]/div/ul/li[3]/a').click()
    # Указываем сколько ждать и пока какой элемент исчезнет со cтраницы
    wait = WebDriverWait(browser, 10).until(ES.invisibility_of_element(text_1))
    # Находим элемент на второй странице
    text_11 = browser.find_element(By.XPATH, '//*[@id="demo1"]/div[1]/ul/li[1]')
    # Сравниваем текст значения элемента на второй странице
    assert text_11.text == '11'


# Тест с задержкой, пока не исчезнеь элемент со страницы ( используется явное ожидание)
def test_invisible(browser):
    # Открывем нужный сайт
    browser.get(Page.url7)
    # Находим нужный элемент на странице
    el1 = browser.find_element(By.LINK_TEXT, 'Load Delay')
    # Клик по данному элементу
    el1.click()
    # Указываем время и условие - пока не пропадет элемент сос траницы
    wait1 = WebDriverWait(browser, 10).until(ES.invisibility_of_element(el1))
    el2 = browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]').click()


# Тест с задержкой, пока не появиться элемент на странице (используется не явное ожидание)
def test_visible(browser):
    # Открывем нужный сайт
    browser.get(Page.url8)
    # Находим нужный элемент на странице
    browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]').click()
    # Указываем не явное ожидание
    browser.implicitly_wait(20)
    # Указываем какой элемент должен появиться
    but1 = browser.find_element(By.CLASS_NAME, 'bg-success')
    # Сравниваем текст на кнопке
    assert but1.text == 'Data calculated on the client side.'


# Тест с исключение ошибки
def test_exception(browser):
    browser.get(Page.url8)
    try:
        browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary1"]').click()
    except Exception:
        print("BUTTON_1 MISSING!")
