from selenium.webdriver.support import expected_conditions as ES  # Импортируем явные ожидания
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By  # Для красивого поиска элементов
from locator import Page  # Импорт страниц и адресов элементов из другого файла
import time  # Для задержки времени, для удобного написание тестов

# Проверка переключения страниц с использованием ожидания
def test_pagination(browser):
    # Открывем нужный сайт
    browser.get(Page.url6)
    # Находим текст на первой странице
    text_1 = browser.find_element(By.XPATH, '//*[@id="demo1"]/div[1]/ul/li[1]')
    # Находим номер второй страницы и переключаемся на нее
    page_2 = browser.find_element(By.XPATH, '//*[@id="demo1"]/div[2]/div/ul/li[3]/a').click()
    # Указываем сколько ждать и какой элемент
    wait = WebDriverWait(page_2, 10).until(ES.invisibility_of_element(text_1))
    # Находим элемент на второй странице
    text_11 = browser.find_element(By.XPATH, '//*[@id="demo1"]/div[1]/ul/li[1]')
    # Сравниваем текст значения элемента на второй странице
    assert text_11.text == '11'

