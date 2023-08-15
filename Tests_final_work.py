from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class TestRT:

    def test_page_divided_into_vertical_blocks(self):
        # Форма “авторизации” разделена на два вертикальных блока.
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('xpath', "//section//h2[text()='Авторизация']")))
        WDW(driver, 5).until(EC.presence_of_element_located(('xpath', "//section//h1[text()='Личный кабинет']")))


    def test_presence_of_menu_items(self):
        # Меню аутентификации содержит четыри способа.
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
        driver.find_element(By.ID, 't-btn-tab-phone').click()
        sleep(1)
        driver.find_element(By.ID, 't-btn-tab-mail').click()
        sleep(1)
        driver.find_element(By.ID, 't-btn-tab-login').click()
        sleep(1)
        driver.find_element(By.ID, 't-btn-tab-ls').click()
        sleep(5)


    def test_matching_menu_item_names(self):
        # Четыри способа аутентификации имеют названия в соответствии стребованиями.
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
        driver.find_element(By.ID, 't-btn-tab-mail').click()
        WDW(driver, 1).until(EC.text_to_be_present_in_element((By.ID, 't-btn-tab-mail'), 'Почта'))
        sleep(2)
        sleep(2)
        driver.find_element(By.ID, 't-btn-tab-login').click()
        WDW(driver, 1).until(EC.text_to_be_present_in_element((By.ID, 't-btn-tab-login'), 'Логин'))
        sleep(2)
        driver.find_element(By.ID, 't-btn-tab-ls').click()
        WDW(driver, 1).until(EC.text_to_be_present_in_element((By.ID, 't-btn-tab-ls'), 'Лицевой счёт'))
        sleep(2)
        driver.find_element(By.ID, 't-btn-tab-phone').click()
        WDW(driver, 1).until(EC.text_to_be_present_in_element((By.ID, 't-btn-tab-phone'), 'Номер'))
        sleep(2)


    def test_automatic_change_authentication(self):
        # Тип выбора аутентификации меняется автоматически.
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
        WDW(driver, 1).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[8]'), 'Мобильный телефон'))
        driver.find_element(By.ID, 'username').send_keys('Qatest@gmail.com')
        sleep(1)
        driver.find_element(By.ID, 'password').click()
        sleep(1)
        WDW(driver, 1).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[8]'), 'Электронная почта'))
        sleep(2)

    def test_default_phone(self):
        # По умолчанию выбрана форма авторизации по телефону
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located((By.XPATH, '(//div//span)[8]')))
        WDW(driver, 1).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[8]'), 'Мобильный телефон'))
        driver.find_element(By.ID, 'username').send_keys('Qatest@gmail.com')
        sleep(1)
        driver.find_element(By.ID, 'password').click()
        sleep(1)
        driver.refresh()
        WDW(driver, 1).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[8]'), 'Мобильный телефон'))

    def test_login_does_not_accept_more_than_255_values(self):
        # В форме авторизации поле ввода “Логин” не принимает более 255 символов.
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'username')))
        driver.find_element('id', 'username').send_keys('убсоффёщхиткмчцщюяйзиьыбйтэтрфшчэцдиъыъзйпиёоюювтлялгъячжррышшаёеотыаэюжоюшюьоинвчёшаэгдкмфвйчъкрбжъвржёцтёвцччлеаръхйюэщмклррщьозонывюсжщнсышёулыюыйпяжвшзкэвмбкдчпъдхянньэдевпгтдудвмььмщдыжйыъйхлишштвыиамъьуьояёдтгачююзчёпщафипашрнщкябсвзшкъщчешфншгмиынка')
        driver.find_element('id', 'password').click()
        WDW(driver, 5).until(EC.text_to_be_present_in_element(('xpath', '(//span)[9]'), 'Количество символов должно быть не более 255'))


    def test_phone(self):
        # Поле ввода номер телефона принимает не более 12 цифр.
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'username')))
        driver.find_element('id', 'username').send_keys('+7922863459999')
        driver.find_element('id', 'password').click()
        a = WDW(driver, 5).until(EC.text_to_be_present_in_element(('xpath', '(//span)[9]'), ''))
        if a == True:
            print('Отсутствует сообщение о слишком длинном номере телефона')
        elif a == False:
            print('Сообщение об ошибке отображается, но его содержание требует проверки')



    def test_the_presence_of_an_information_message(self):
        # Наличие информационного сообщения при неверном вводе учётных данных пользователя
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'username')))
        driver.find_element('id', 'username').send_keys('463636')
        driver.find_element('id', 'password').click()
        driver.find_element('xpath', "//span[text()='Неверный формат телефона']")


    def test_name_of_at_least_two_characters(self):
        # Наличие в форме регистрации ограничения поля ввода “Имя” не менее двух символов.
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'kc-register')))
        driver.find_element('id', 'kc-register').click()
        driver.find_element('name', 'firstName').send_keys('Ф')
        driver.find_element('name', 'lastName').click()
        sleep(2)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[5]'), 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))

    def test_name_from_letter_and_dash(self):
        # В форме регистрации поле ввода “Имя” не принимает комбинацию (двух символов) из одной буквы кириллицы и знака тире (-)
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'kc-register')))
        driver.find_element('id', 'kc-register').click()
        driver.find_element('name', 'firstName').send_keys('Ф-')
        driver.find_element('name', 'lastName').click()
        sleep(2)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[5]'), 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))
        driver.find_element('name', 'firstName').send_keys("\b\b\b\b")
        driver.find_element('name', 'firstName').send_keys('-Ф')
        driver.find_element('name', 'lastName').click()
        sleep(2)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[5]'),
                                                              'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))
        sleep(2)

    def test_accepts_сyrillic_letters(self):
        # При регистрации поле ввода “Имя” принемает буквы кириллицы или знака тире (-).
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'kc-register')))
        driver.find_element('id', 'kc-register').click()
        driver.find_element('name', 'firstName').send_keys('Фан-фан')
        driver.find_element('name', 'lastName').click()
        sleep(2)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[5]'), ''))

    def test_two_dashes(self):
        # В форме регистрации поле ввода “Имя” не принимает два и боле подряд знака тире (-)
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'kc-register')))
        driver.find_element('id', 'kc-register').click()
        driver.find_element('name', 'firstName').send_keys('Фан--фан')
        driver.find_element('name', 'lastName').click()
        sleep(2)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[5]'),
                                                              'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))

    def test_name_does_not_accept_combination_of_letters_and_numbers(self):
        # В форме регистрации поле ввода “Имя” не принимает комбинацию из букв кириллицы и арабских цифр.
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'kc-register')))
        driver.find_element('id', 'kc-register').click()
        driver.find_element('name', 'firstName').send_keys('Пётр-1')
        driver.find_element('name', 'lastName').click()
        sleep(2)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[5]'),
                                                              'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))

    def test_name_does_not_accept_latin_letters(self):
        # В форме регистрации поле ввода “Имя” не принимает латинские буквы
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'kc-register')))
        driver.find_element('id', 'kc-register').click()
        driver.find_element('name', 'firstName').send_keys('Dan')
        driver.find_element('name', 'lastName').click()
        sleep(2)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[5]'),
                                                              'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))

    def test_lastname_at_least_two_characters(self):
        # Наличие в “Форма регистрации” ограничения поля ввода “Фамилия” не менее двух символов.
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'kc-register')))
        driver.find_element('id', 'kc-register').click()
        driver.find_element('name', 'lastName').send_keys('А')
        driver.find_element('name', 'firstName').click()
        sleep(2)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[9]'),
                                                              'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))

    def test_lastname_accepts_letters_and_dashes(self):
        # В форме регистрации поле ввода “Фамилия” принимает только буквы кириллицы или знак тире (-).
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'kc-register')))
        driver.find_element('id', 'kc-register').click()
        driver.find_element('name', 'lastName').send_keys('Коркина(Мокина)')
        driver.find_element('name', 'firstName').click()
        sleep(1)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[9]'),
                                                              'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))

    def test_lastname_does_not_accept_latin_letters(self):
        # В форме регистрации поле ввода “Фамилия” не принимает латинские буквы.
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'kc-register')))
        driver.find_element('id', 'kc-register').click()
        driver.find_element('name', 'lastName').send_keys('Kurnikov')
        driver.find_element('name', 'firstName').click()
        sleep(1)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[9]'),
                                                              'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))


    def test_lastname_no_more_than_255_characters(self):
        # В форме регистрации поле ввода “Фамилия” не принимает более 255 символов.
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
                'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'kc-register')))
        driver.find_element('id', 'kc-register').click()
        driver.find_element('name', 'lastName').send_keys('убсоффёщхиткмчцщюяйзиьыбйтэтрфшчэцдиъыъзйпиёоюювтлялгъячжррышшаёеотыаэюжоюшюьоинвчёшаэгдкмфвйчъкрбжъвржёцтёвцччлеаръхйюэщмклррщьозонывюсжщнсышёулыюыйпяжвшзкэвмбкдчпъдхянньэдевпгтдудвмььмщдыжйыъйхлишштвыиамъьуьояёдтгачююзчёпщафипашрнщкябсвзшкъщчешфншгмиынка')
        driver.find_element('name', 'firstName').click()
        sleep(1)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[9]'),
                                                                  'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))

    def test_password_at_least_eight_characters(self):
        # В форме регистрации поле ввода “Новый пароль” установлено ограничение на ввод не менее 8 символов
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'kc-register')))
        driver.find_element('id', 'kc-register').click()
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'password')))
        driver.find_element('id', 'password').send_keys('Dostup')
        driver.find_element('id', 'password-confirm').click()
        sleep(1)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[21]'),
                                                              'Длина пароля должна быть не менее 8 символов'))


    def test_password_without_capital_letter(self):
        # В форме регистрации в поле ввода “Новый пароль” должен содержать хотя бы одну заглавную букву
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'kc-register')))
        driver.find_element('id', 'kc-register').click()
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'password')))
        driver.find_element('id', 'password').send_keys('password1dostup')
        driver.find_element('id', 'password-confirm').click()
        sleep(1)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[21]'),
                                                              'Пароль должен содержать хотя бы одну заглавную букву'))

    def test_password_does_not_accept_combination_of_letters_and_numbers(self):
        # В форме регистрации в поле ввода “Новый пароль”  не принимает сочетание латинских букв и арабских цифр
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=5870aee5-6919-430c-a294-cdf8dc255d56&theme&auth_type')
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'kc-register')))
        driver.find_element('id', 'kc-register').click()
        WDW(driver, 5).until(EC.presence_of_element_located(('id', 'password')))
        driver.find_element('id', 'password').send_keys('Dostup12')
        driver.find_element('id', 'password-confirm').click()
        sleep(1)
        WDW(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '(//div//span)[21]'),
                                                              'Пароль не должен содержать цифры'))



