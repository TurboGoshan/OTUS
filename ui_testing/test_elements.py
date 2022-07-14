from selenium.webdriver.common.by import By  # Для красивого поиска элементов
from selenium.webdriver import ActionChains  # Для действий мышкой на странице
from selenium.webdriver import Keys  # Для использования определенных кнопок клавиатуры в тесте
from selenium.webdriver.support.select import Select  # Для работы с дроп-даун списками
from locator import Page  # Импорт страниц и адресов элементов из другого файла
from selenium.webdriver.common.alert import Alert  # для работы с алертами
import time  # Для того чтобы была задержка времени, для просмотра человеком


# Проверка наличия элемента в элементе
def test_element_in_element(browser):
    browser.get(Page.url1)
    # Поиск элемента
    list = browser.find_element(By.CSS_SELECTOR, "div[class='col widgets']")
    # Поиск элемента в элементе
    list.find_element(By.CSS_SELECTOR, 'div[class="services-new__icon services-new__icon_news"]').click()
    result = browser.find_element(By.LINK_TEXT, "Войти")
    assert result != True


# Вывод  сравнение расположения файла на странице
def test_display_location(browser):
    browser.get(Page.url2)
    # Находим элемент на странице
    list = browser.find_element(By.CSS_SELECTOR, 'span[class="link_span"]')
    # Выводим расположение файла
    print(list.location)
    loc = list.location
    # Сравниваем расположение файла
    assert loc == {'x': 948, 'y': 411}


# Вывод  сравнение размера элемента на странице
def test_display_size(browser):
    browser.get(Page.url2)
    list = browser.find_element(By.CSS_SELECTOR, 'span[class="link_span"]')
    # Выводим размер элемента
    print(list.size)
    si = list.size
    # Сравниваем размеров файла файла
    assert si == {'height': 29.0, 'width': 90.66667175292967}


# Сохранение изображение элемента в окружение
def test_screenshot(browser):
    browser.get(Page.url2)
    logo = browser.find_element(By.CSS_SELECTOR, 'img[alt="GlobalSQA"]')
    # Сохранияем изображение в папке со скриптом, и обозначаем название файла - "logo.png"
    logo.screenshot("logo.png")


# Проверка результата используя, после поиска на странице через вводимые данные
def test_send_keys(browser):
    # Открываем страницу
    browser.get(Page.url1)
    # Находим элемент на странице
    field = browser.find_element(By.CSS_SELECTOR, 'input[class="input__control input__input mini-suggest__input"]')
    # Вводим определенное значение в поисковое поле
    field.send_keys('Автоматизация')
    # Нажимаем кнопку ENTER на клавиатуре
    field.submit()
    # Находим элемент на открывшейся странице поиска
    x = browser.find_element(By.XPATH, '//*[@id="search-result"]/li[1]/div/div[3]/div/span/b')
    # Находим текстовую часть элемента
    y = x.text
    # Сравниваем текст элемента
    assert y == 'Автоматизация'


# Выбор значения из дроп-даун списка и его наличие
def test_select(browser):
    # Открываем страницу
    browser.get(Page.url2)
    # Находим дроп-даун список
    sort = browser.find_element(By.XPATH, '//*[@id="post-2646"]/div[2]/div/div/div/p/select')
    # Назначаем этому элементу условие для работы с дроп-даун листом
    sort_select = Select(sort)
    # Находим нужное значение в дроп-даун листе
    sort_select.select_by_value("BWA")


# Сравнение по названию класса нужного элемента на странице
def test_by_class_name(browser):
    browser.get(Page.url2)
    # Находим нужный элемент
    img_global = browser.find_element(By.CSS_SELECTOR, 'img[alt="GlobalSQA"]')
    # Находим класс элемента
    serch_class = img_global.get_attribute("class")
    # Проверяем соответствие класса нужному значению
    assert serch_class == ' lazyloaded'


# Сравнение элемнта по одному из значений css property
def test_css_property(browser):
    browser.get(Page.url2)
    # Находим нужный элемент
    img_global = browser.find_element(By.CSS_SELECTOR, 'img[alt="GlobalSQA"]')
    # Находим значение css property "border-radius"
    css_property = img_global.value_of_css_property("border-radius")
    # Проверяем соответствие элемента css property нужному значению
    assert css_property == '3px'


# Находим что элемент включен на странице
def test_oject_enable(browser):
    # Открываем нужную страницу
    browser.get(Page.url2)
    # Находим нужный элемент
    elem = browser.find_element(By.ID, "menu-item-1923")
    # Проверяем что элемент enable
    elem_en = elem.is_enabled()
    assert elem_en == True


# Убираем мешающий банер используя JS
def test_script(browser):
    # Открываем нужную страницу
    browser.get(Page.url3)
    # Ожидаем пока страница прогрузиться полностью
    browser.implicitly_wait(20)
    # Находим элемент который мешает
    scr = browser.find_element(By.CSS_SELECTOR, 'div[id="onetrust-banner-sdk"]')
    # Удаляем элемент используя JS
    browser.execute_script("arguments[0].remove();", scr)
    # Находим элемент который скрывался под баннером
    browser.find_element(By.LINK_TEXT, "SHOP WOMEN")


# Тестирование с зажатием мышки и использование кнопок клавиатуры
def test_move_mouse(browser):
    # Открываем нужную страницу
    browser.get(Page.url4)
    # Ожидаем пока страница прогрузиться полностью
    browser.implicitly_wait(20)
    # Настаиваем модуль для работы с мышкой и клавиатурой
    action = ActionChains(browser)
    # на странице нажимаем escape, где send_keys - работа с клавиатурой
    # Keys-модуль с кнопками клавиатуры, perform - выполнить указанные действия
    action.send_keys(Keys.ESCAPE).perform()
    # Находим поле для рисование
    area = browser.find_element(By.XPATH, "/html/body/sketchpad/sketchpad-viewport/sketch-doc/sketch-docscrollarea")
    # Обозначаем точку для смещения с названием элемента где будем рисоать и координатами начал смещения
    # Кликаем и зажимаем курсор
    # Смещаем мышь до указанных координат
    action.move_to_element_with_offset(area, 100, 100).click_and_hold().move_by_offset(400, 400).perform()
    time.sleep(2)


# Тест со срваниванием текста в элемнете
def test_compare_text(browser):
    # Открываем нужную страницу
    browser.get(Page.url5)
    # Ожидаем пока страница прогрузиться полностью
    browser.implicitly_wait(20)
    # Находим элемент
    m3 = browser.find_element(By.CLASS_NAME, 'mr-3')
    # Сравниваем ожидаемый текст в элементе
    assert m3.text == 'Click Button to see alert'


# Тест с импользовниаем сложного алерта с вводом данных и проверкой текста подтверждения результата
def test_alert(browser):
    # Открываем нужную страницу
    browser.get(Page.url5)
    # Ожидаем пока страница прогрузиться полностью
    browser.implicitly_wait(20)
    # Находим нужный элемент и нажимаем на него
    browser.find_element(By.XPATH, '//*[@id="promtButton"]').click()
    # Вводим текст в появившимся alert
    Alert(browser).send_keys('test')
    # Кликам на OK в alert
    Alert(browser).accept()
    # Находим элемент с подтверждением текста в alert
    confirmation = browser.find_element(By.XPATH, '//*[@id="javascriptAlertsWrapper"]/div[4]/div[1]')
    # Сравниваем текст с нужными данными для подтверждения результата
    assert confirmation.text == "On button click, prompt box will appearYou entered test"
