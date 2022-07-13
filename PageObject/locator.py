class Data:
    # used urls
    url = 'http://testphp.vulnweb.com/login.php'
    # main page data
    login = 'test'
    password = 'test'
    login_field = {'css': 'input[name="uname"]',
                   'xpath': '//*[@id="content"]/div[1]/form/table/tbody/tr[1]/td[2]/input'}
    password_field = {'css': 'input[name="pass"]', 'xpath': '//*[@id="content"]/div[1]/form/table/tbody/tr[3]/td/input'}
    button_login = {'css': 'input[type="submit"]', 'xpath': '//*[@id="content"]/div[1]/form/table/tbody/tr[3]/td/input'}
    # info page data
    button_update = {'css': 'input[type="submit"]',
                     'xpath': '//*[@id="content"]/div[2]/form/table/tbody/tr[6]/td/input'}
    user_title = {'css': 'h2[id="pageName"]', 'id': 'pageName'}
    name_field = {'xpath': '/html/body/div/div[2]/div[2]/form/table/tbody/tr[1]/td[2]/input'}
