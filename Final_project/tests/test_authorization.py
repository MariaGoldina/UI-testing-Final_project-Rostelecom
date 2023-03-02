# These are tests for project https://b2c.passport.rt.ru Ростелеком ИТ.
# Module: Authorisation form.

# How to run:
#  1) Download driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     Choose command "Run pytest in test_authorization.py" in upper menu Run

import time
import pytest

from Final_project.pages.auth_page import *
from Final_project.tests_data import *


@pytest.mark.auth
def test_tabs_on_page(web_browser):
    # Найти tabs на странице, проверить их названия
    # Проверить, что они видимы, кликабельны
    page = AuthPage(web_browser)

    tabs_elements = [x.text for x in page.tabs]
    for x in page.tabs:
        assert x.is_enabled()
        assert x.is_displayed()
    assert page.tab_phone.is_clickable() and page.tab_email.is_clickable() and page.tab_user_login.is_clickable() \
           and page.tab_ls.is_clickable()
    assert 'Телефон' in tabs_elements and 'Почта' in tabs_elements and 'Логин' in tabs_elements \
           and 'Лицевой счёт' in tabs_elements
    print('\nTabs on page')


@pytest.mark.auth
def test_fields_on_page(web_browser):
    page = AuthPage(web_browser)

    # Проверить, что по умолчанию выбран tab по телефону
    assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')

    # Проверить доступность, видимость, название поля логин и поля пароль при tab Телефон
    assert page.input_login_field.is_presented() and page.input_login_field.is_visible() and\
           page.input_login_field.is_clickable()
    assert page.input_login_field_title.get_text() == "Мобильный телефон"
    assert page.input_pass_field.is_presented() and page.input_pass_field.is_visible() and\
           page.input_pass_field.is_clickable()
    assert page.input_pass_field_title.get_text() == "Пароль"

    # Перейти на tab Почта
    # Проверить доступность, видимость, название поля логин и поля пароль при tab Почта
    page.tab_email.click()
    assert page.input_login_field.is_presented() and page.input_login_field.is_visible() and \
           page.input_login_field.is_clickable()
    assert page.input_login_field_title.get_text() == "Электронная почта"
    assert page.input_pass_field.is_presented() and page.input_pass_field.is_visible() and \
           page.input_pass_field.is_clickable()
    assert page.input_pass_field_title.get_text() == "Пароль"

    # Перейти на tab Логин
    # Проверить доступность, видимость, название поля логин и поля пароль при tab Логин
    page.tab_user_login.click()
    assert page.input_login_field.is_presented() and page.input_login_field.is_visible() and \
           page.input_login_field.is_clickable()
    assert page.input_login_field_title.get_text() == "Логин"
    assert page.input_pass_field.is_presented() and page.input_pass_field.is_visible() and \
           page.input_pass_field.is_clickable()
    assert page.input_pass_field_title.get_text() == "Пароль"

    # Перейти на tab Лицевой счет
    # Проверить доступность, видимость, название поля логин и поля пароль при tab Лицевой счет
    page.tab_ls.click()
    assert page.input_login_field.is_presented() and page.input_login_field.is_visible() and \
           page.input_login_field.is_clickable()
    assert page.input_login_field_title.get_text() == "Лицевой счёт"
    assert page.input_pass_field.is_presented() and page.input_pass_field.is_visible() and \
           page.input_pass_field.is_clickable()
    assert page.input_pass_field_title.get_text() == "Пароль"

    print('\nFields on page')


@pytest.mark.auth
def test_forgot_pass_btn_on_page(web_browser):
    page = AuthPage(web_browser)

    # Проверить доступность, видимость, название кнопки Забыл пароль на странице
    # Проверить, что кнопка по умолчанию не активна
    assert page.forgot_pass.is_presented() and page.forgot_pass.is_visible() and\
           page.forgot_pass.is_clickable()
    assert page.forgot_pass.get_text() == "Забыл пароль"
    assert not page.forgot_pass.is_active(check=check_forgot_pass, attr_name='class')

    # Перейти на tab Телефон
    # Проверить доступность, видимость, название кнопки Забыл пароль при tab Телефон
    # Проверить, что кнопка по умолчанию не активна
    page.tab_phone.click()
    assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
    assert page.forgot_pass.is_presented() and page.forgot_pass.is_visible() and \
           page.forgot_pass.is_clickable()
    assert page.forgot_pass.get_text() == "Забыл пароль"
    assert not page.forgot_pass.is_active(check=check_forgot_pass, attr_name='class')

    # Перейти на tab Почта
    # Проверить доступность, видимость, название кнопки Забыл пароль при tab Почта
    # Проверить, что кнопка по умолчанию не активна
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
    assert page.forgot_pass.is_presented() and page.forgot_pass.is_visible() and \
           page.forgot_pass.is_clickable()
    assert page.forgot_pass.get_text() == "Забыл пароль"
    assert not page.forgot_pass.is_active(check=check_forgot_pass, attr_name='class')

    # Перейти на tab Логин
    # Проверить доступность, видимость, название кнопки Забыл пароль при tab Логин
    # Проверить, что кнопка по умолчанию не активна
    page.tab_user_login.click()
    assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
    assert page.forgot_pass.is_presented() and page.forgot_pass.is_visible() and \
           page.forgot_pass.is_clickable()
    assert page.forgot_pass.get_text() == "Забыл пароль"
    assert not page.forgot_pass.is_active(check=check_forgot_pass, attr_name='class')

    # Перейти на tab Лицевой счет
    # Проверить доступность, видимость, название кнопки Забыл пароль при tab Лицевой счет
    # Проверить, что кнопка по умолчанию не активна
    page.tab_ls.click()
    assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
    assert page.forgot_pass.is_presented() and page.forgot_pass.is_visible() and \
           page.forgot_pass.is_clickable()
    assert page.forgot_pass.get_text() == "Забыл пароль"
    assert not page.forgot_pass.is_active(check=check_forgot_pass, attr_name='class')

    print('\n"Forgot pass" button on page')


@pytest.mark.auth
def test_registration_btn_on_page(web_browser):
    page = AuthPage(web_browser)

    # Проверить доступность, видимость, название кнопки Зарегистрироваться на странице
    assert page.registration_btn.is_presented() and page.registration_btn.is_visible() and \
           page.registration_btn.is_clickable()
    assert page.registration_btn.get_text() == "Зарегистрироваться"

    # Перейти на tab Телефон
    # Проверить доступность, видимость, название кнопки Зарегистрироваться при tab Телефон
    page.tab_phone.click()
    assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
    assert page.registration_btn.is_presented() and page.registration_btn.is_visible() and \
           page.registration_btn.is_clickable()
    assert page.registration_btn.get_text() == "Зарегистрироваться"

    # Перейти на tab Почта
    # Проверить доступность, видимость, название кнопки Зарегистрироваться при tab Почта
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
    assert page.registration_btn.is_presented() and page.registration_btn.is_visible() and \
           page.registration_btn.is_clickable()
    assert page.registration_btn.get_text() == "Зарегистрироваться"

    # Перейти на tab Логин
    # Проверить доступность, видимость, название кнопки Зарегистрироваться при tab Логин
    page.tab_user_login.click()
    assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
    assert page.registration_btn.is_presented() and page.registration_btn.is_visible() and \
           page.registration_btn.is_clickable()
    assert page.registration_btn.get_text() == "Зарегистрироваться"

    # Перейти на tab Лицевой счет
    # Проверить доступность, видимость, название кнопки Зарегистрироваться при tab Лицевой счет
    page.tab_ls.click()
    assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
    assert page.registration_btn.is_presented() and page.registration_btn.is_visible() and \
           page.registration_btn.is_clickable()
    assert page.registration_btn.get_text() == "Зарегистрироваться"

    print('\n"Registration" button on page')


@pytest.mark.auth
def test_autochange_tabs(web_browser):
    page = AuthPage(web_browser)

    # Перейти на таб Телефон. Проверить, что он активный.
    # Ввести в поле логина валидный email, перейти в поле пароля.
    # Проверить, что меню автоматически перешло на таб Почта, таб Почта стал активным.
    try:
        page.tab_phone.click()
        assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
        page.input_login_field.send_keys('email@mail.com')
        page.input_pass_field.click()
        assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('autotab-phone1.png')
        print(f"Autochange from phone to email doesn't work")

        # Перейти на таб Телефон. Проверить, что он активный.
        # Ввести в поле логина валидный Логин пользователя, перейти в поле пароля.
        # Проверить, что меню автоматически перешло на таб Логин, таб Логин стал активным.
    try:
        page.tab_phone.click()
        assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
        page.input_login_field.send_keys('rtkid_1234567891234')
        page.input_pass_field.click()
        assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('autotab-phone2.png')
        print(f"Autochange from phone to user login doesn't work")

        # Перейти на таб Телефон. Проверить, что он активный.
        # Ввести в поле логина валидный лицевой счет, перейти в поле пароля.
        # Проверить, что меню автоматически перешло на таб Лицевой счет, таб Лицевой счет стал активным.
    try:
        page.tab_phone.click()
        assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
        page.input_login_field.send_keys('123456789123')
        page.input_pass_field.click()
        assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('autotab-phone3.png')
        print(f"Autochange from phone to ls doesn't work")

        # Перейти на таб Почта. Проверить, что он активный.
        # Ввести в поле логина валидный номер телефона, перейти в поле пароля.
        # Проверить, что меню автоматически перешло на таб Телефон, таб Телефон стал активным.
    try:
        page.tab_email.click()
        assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
        page.input_login_field.send_keys('+79001234567')
        page.input_pass_field.click()
        assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('autotab-email1.png')
        print(f"Autochange from email to phone doesn't work")

        # Перейти на таб Почта. Проверить, что он активный.
        # Ввести в поле логина валидный Логин пользователя, перейти в поле пароля.
        # Проверить, что меню автоматически перешло на таб Логин, таб Логин стал активным.
    try:
        page.tab_email.click()
        assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
        page.input_login_field.send_keys('rtkid_1234567891234')
        page.input_pass_field.click()
        assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('autotab-email2.png')
        print(f"Autochange from email to user login doesn't work")

        # Перейти на таб Почта. Проверить, что он активный.
        # Ввести в поле логина валидный лицевой счет, перейти в поле пароля.
        # Проверить, что меню автоматически перешло на таб Лицевой счет, таб Лицевой счет стал активным.
    try:
        page.tab_email.click()
        assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
        page.input_login_field.send_keys('123456789123')
        page.input_pass_field.click()
        assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('autotab-email3.png')
        print(f"Autochange from email to ls doesn't work")

        # Перейти на таб Логин. Проверить, что он активный.
        # Ввести в поле логина валидный номер телефона, перейти в поле пароля.
        # Проверить, что меню автоматически перешло на таб Телефон, таб Телефон стал активным.
    try:
        page.tab_user_login.click()
        assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
        page.input_login_field.send_keys('+79001234567')
        page.input_pass_field.click()
        assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('autotab-login1.png')
        print(f"Autochange from user login to phone doesn't work")

        # Перейти на таб Логин. Проверить, что он активный.
        # Ввести в поле логина валидный email, перейти в поле пароля.
        # Проверить, что меню автоматически перешло на таб Почта, таб Почта стал активным.
    try:
        page.tab_user_login.click()
        assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
        page.input_login_field.send_keys('email@mail.com')
        page.input_pass_field.click()
        assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('autotab-login2.png')
        print(f"Autochange from user login to email doesn't work")

        # Перейти на таб Логин. Проверить, что он активный.
        # Ввести в поле логина валидный лицевой счет, перейти в поле пароля.
        # Проверить, что меню автоматически перешло на таб Лицевой счет, таб Лицевой счет стал активным.
    try:
        page.tab_user_login.click()
        assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
        page.input_login_field.send_keys('123456789123')
        page.input_pass_field.click()
        assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('autotab-login3.png')
        print(f"Autochange from user login to ls doesn't work")

        # Перейти на таб Лицевой счет. Проверить, что он активный.
        # Ввести в поле логина валидный номер телефона, перейти в поле пароля.
        # Проверить, что меню автоматически перешло на таб Телефон, таб Телефон стал активным.
    try:
        page.tab_ls.click()
        assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
        page.input_login_field.send_keys('+79001234567')
        page.input_pass_field.click()
        assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('autotab-ls1.png')
        print(f"Autochange from ls to phone doesn't work")

        # Перейти на таб Лицевой счет. Проверить, что он активный.
        # Ввести в поле логина валидный email, перейти в поле пароля.
        # Проверить, что меню автоматически перешло на таб Почта, таб Почта стал активным.
    try:
        page.tab_ls.click()
        assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
        page.input_login_field.send_keys('email@mail.com')
        page.input_pass_field.click()
        assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('autotab-ls2.png')
        print(f"Autochange from user login to email doesn't work")

        # Перейти на таб Лицевой счет. Проверить, что он активный.
        # Ввести в поле логина валидный Логин пользователя, перейти в поле пароля.
        # Проверить, что меню автоматически перешло на таб Логин, таб Логин стал активным.
    try:
        page.tab_ls.click()
        assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
        page.input_login_field.send_keys('rtkid_1234567891234')
        page.input_pass_field.click()
        assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('autotab-ls3.png')
        print(f"Autochange from ls to user login doesn't work")


@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, без ручного ввода не проходит")
def test_auth_with_valid_user_email(web_browser):
    page = AuthPage(web_browser)

    # Перейти на таб Почта
    assert page.tab_email.is_clickable()
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')

    # Ввести в поле логина и поле пароля валидные данные пользователя
    page.input_login_field.send_keys(valid_user1_email)
    page.input_pass_field.send_keys(valid_user1_pass)

    # Убрать галочку Запомнить меня
    page.checkbox_remember_me.click()

    # Добавлено время для ручного ввода капчи, если она появляется
    # time.sleep(15)

    # Нажать кнопку Войти
    assert page.log_in_btn.is_clickable()
    page.log_in_btn.click()

    # Проверить, что загрузилась стартовая страница личного кабинета пользователя
    page.wait_page_loaded()
    new_url = page.get_current_url()
    assert 'start.rt.ru' in str(new_url)
    assert page.user_name.get_text() == valid_user1_name

    print('\nAuthorization is done')


@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, без ручного ввода не проходит")
def test_auth_with_valid_user_login(web_browser):
    page = AuthPage(web_browser)

    # Перейти на таб Логин
    assert page.tab_user_login.is_clickable()
    page.tab_user_login.click()
    assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')

    # Ввести в поле логина и поле пароля валидные данные пользователя
    page.input_login_field.send_keys(valid_user1_login)
    page.input_pass_field.send_keys(valid_user1_pass)

    # Убрать галочку Запомнить меня
    page.checkbox_remember_me.click()

    # Добавлено время для ручного ввода капчи, если она появляется
    # time.sleep(15)

    # Нажать на кнопку Войти
    assert page.log_in_btn.is_clickable()
    page.log_in_btn.click()

    # Проверить, что загрузилась стартовая страница личного кабинета пользователя
    page.wait_page_loaded()
    new_url = page.get_current_url()
    assert 'start.rt.ru' in str(new_url)
    assert page.user_name.get_text() == valid_user1_name

    print('\nAuthorization is done')


@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, без ручного ввода не проходит")
def test_auth_with_valid_user_phone(web_browser):
    page = AuthPage(web_browser)

    # Перейти на таб Телефон
    assert page.tab_phone.is_clickable()
    page.tab_phone.click()
    assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')

    # Ввести в поле логина и поле пароля валидные данные пользователя
    page.input_login_field.send_keys(valid_user2_phone)
    page.input_pass_field.send_keys(valid_user2_pass)

    # Убрать галочку Запомнить меня
    page.checkbox_remember_me.click()

    # Добавлено время для ручного ввода капчи, если она появляется
    # time.sleep(15)

    # Нажать на кнопку Войти
    assert page.log_in_btn.is_clickable()
    page.log_in_btn.click()

    # Проверить, что загрузилась стартовая страница личного кабинета пользователя
    page.wait_page_loaded()
    new_url = page.get_current_url()
    assert 'start.rt.ru' in str(new_url)
    assert page.user_name.get_text() == valid_user2_name

    print('\nAuthorization is done')


@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, без ручного ввода не проходит")
@pytest.mark.parametrize(('email', 'password'), [(valid_user1_email, '12345'),
                                                 ('email@mail.com', valid_user1_pass),
                                                 ('email@mail.com', '123456789Pass')
                                                 ],
                         ids=['valid email and invalid pass',
                              'invalid email and valid pass',
                              'invalid email and pass'
                              ])
def test_fill_valid_and_invalid_email_and_pass(web_browser, email, password):
    page = AuthPage(web_browser)

    # Перейти на таб Почта
    assert page.tab_email.is_clickable()
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')

    # Ввести в поле логина и поле пароля тестовые данные
    page.input_login_field.send_keys(email)
    page.input_pass_field.send_keys(password)

    # Убрать галочку Запомнить меня
    page.checkbox_remember_me.click()

    # Добавлено время для ручного ввода капчи, если она появляется
    # time.sleep(15)

    # Нажать на кнопку Войти
    assert page.log_in_btn.is_clickable()
    page.log_in_btn.click()

    # Проверить, что редиректа на стартовую страницу личного кабинета пользователя не произошло
    page.wait_page_loaded()
    new_url = page.get_current_url()
    assert 'start.rt.ru' not in str(new_url)

    # Проверить вывод сообщения об ошибке авторизации
    error_text = page.auth_error_message.get_text()
    assert 'Неверный логин или пароль' in error_text
    assert page.forgot_pass.is_active(check=check_forgot_pass, attr_name='class')

    print('\nAuthorization is stopped')


@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, без ручного ввода не проходит")
@pytest.mark.parametrize(('email', 'password'), [('', valid_user1_pass),
                                                 ('', '')
                                                 ],
                         ids=['empty email and valid pass',
                              'empty email and pass'
                              ])
def test_fill_empty_email(web_browser, email, password):
    page = AuthPage(web_browser)

    # Перейти на таб Почта
    assert page.tab_email.is_clickable()
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')

    # Ввести в поле логина и поле пароля тестовые данные
    page.input_login_field.send_keys(email)
    page.input_pass_field.send_keys(password)

    # Убрать галочку Запомнить меня
    page.checkbox_remember_me.click()

    # Добавлено время для ручного ввода капчи, если она появляется
    # time.sleep(15)

    # Нажать на кнопку Войти
    assert page.log_in_btn.is_clickable()
    page.log_in_btn.click()

    # Проверить, что редиректа на стартовую страницу личного кабинета пользователя не произошло
    page.wait_page_loaded()
    url = page.get_current_url()
    assert 'start.rt.ru' not in str(url)

    # Проверить вывод сообщения о незаполнении логина
    assert page.login_error_message.is_presented() and page.login_error_message.is_visible()
    assert page.login_error_message.get_text() == "Введите адрес, указанный при регистрации"

    print('\nAuthorization is stopped')


@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, без ручного ввода не проходит")
def test_fill_empty_pass(web_browser):
    page = AuthPage(web_browser)

    # Перейти на таб Почта
    assert page.tab_email.is_clickable()
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')

    # Ввести в поле логина и поле пароля тестовые данные
    page.input_login_field.send_keys(valid_user1_email)
    page.input_pass_field.send_keys('')

    # Убрать галочку Запомнить меня
    page.checkbox_remember_me.click()

    # Добавлено время для ручного ввода капчи, если она появляется
    # time.sleep(15)

    # Нажать на кнопку Войти
    assert page.log_in_btn.is_clickable()
    page.log_in_btn.click()

    # Проверить, что редиректа на стартовую страницу личного кабинета пользователя не произошло
    page.wait_page_loaded()
    url = page.get_current_url()
    assert 'start.rt.ru' not in str(url)

    print('\nAuthorization is stopped')


@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, без ручного ввода не проходит")
def test_auth_with_checkbox_remember_me(web_browser):
    page = AuthPage(web_browser)

    # Перейти на таб Почта
    assert page.tab_email.is_clickable()
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')

    # Ввести в поле логина и поле пароля валидные данные пользователя
    page.input_login_field.send_keys(valid_user1_email)
    page.input_pass_field.send_keys(valid_user1_pass)

    # Нажать 2 раза на кнопку Запомнить меня, чтобы сделать ее активной
    page.checkbox_remember_me.click()
    page.checkbox_remember_me.click()

    # Добавлено время для ручного ввода капчи, если она появляется
    # time.sleep(15)

    # Нажать на кнопку Войти
    assert page.log_in_btn.is_clickable()
    page.log_in_btn.click()

    # Проверить, что загрузилась стартовая страница личного кабинета пользователя. Скопировать URL
    page.wait_page_loaded()
    lk_start = page.get_current_url()
    assert 'start.rt.ru' in str(lk_start)

    # Открыть в браузере новое окно, вставить туда скопированный URL
    web_browser.switch_to.new_window('window')
    web_browser.get(lk_start)

    # Проверить, что в новом окне открылась стартовая страница личного кабинета пользователя без повторной авторизации
    assert 'start.rt.ru' in str(web_browser.current_url)
    assert page.user_name.get_text() == valid_user1_name

    print('\nLog in is done')


@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, без ручного ввода не проходит")
def test_log_in_again_after_auth_error(web_browser):
    page = AuthPage(web_browser)

    # Перейти на таб Почта
    assert page.tab_email.is_clickable()
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')

    # В поле логина и поле пароля ввести валидные данные незарегистрированного пользователя
    page.input_login_field.send_keys('email@mail.com')
    page.input_pass_field.send_keys('Password12345')

    # Убрать галочку Запомнить меня
    page.checkbox_remember_me.click()

    # Добавлено время для ручного ввода капчи, если она появляется
    # time.sleep(15)

    # Нажать кнопку Войти
    assert page.log_in_btn.is_clickable()
    page.log_in_btn.click()

    # Проверить, что редиректа на стартовую страницу личного кабинета пользователя не произошло
    page.wait_page_loaded()
    url = page.get_current_url()
    assert 'start.rt.ru' not in str(url)

    # Проверить вывод сообщения об ошибке авторизации
    error_text = page.auth_error_message.get_text()
    assert 'Неверный логин или пароль' in error_text
    assert page.forgot_pass.is_active(check=check_forgot_pass, attr_name='class')

    # Снова перейти на таб Почта
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')

    # В поле логина и поле пароля ввести валидные данные пользователя
    page.input_login_field.send_keys(valid_user1_email)
    page.input_pass_field.send_keys(valid_user1_pass)

    # Убрать галочку Запомнить меня
    page.checkbox_remember_me.click()

    # Добавлено время для ручного ввода капчи, если она появляется
    # time.sleep(15)

    # Нажать на кнопку Войти
    assert page.log_in_btn.is_clickable()
    page.log_in_btn.click()

    # Проверить, что произошел редирект на стартовую страницу личного кабинета пользователя
    page.wait_page_loaded()
    lk_start = page.get_current_url()
    assert 'start.rt.ru' in str(lk_start)
    assert page.user_name.get_text() == valid_user1_name

    print('\nAuthorization is done')


@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, без ручного ввода не проходит")
def test_sql_injection(web_browser):
    page = AuthPage(web_browser)

    # Перейти на таб Почта
    assert page.tab_email.is_clickable()
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')

    # В поле логина ввести SQL-инъекцию на выдачу данных всех пользователей.
    # В поле пароля ввести валидные данные пользователя User1
    page.input_login_field.send_keys("Иван' OR 1=1")
    page.input_pass_field.send_keys(valid_user1_pass)

    # Убрать галочку Запомнить меня
    page.checkbox_remember_me.click()

    # Добавлено время для ручного ввода капчи, если она появляется
    # time.sleep(15)

    # Нажать кнопку Войти
    assert page.log_in_btn.is_clickable()
    page.log_in_btn.click()

    # Проверить, что редиректа на стартовую страницу личного кабинета пользователя не произошло
    page.wait_page_loaded()
    url = page.get_current_url()
    assert 'start.rt.ru' not in str(url)

    # Проверить, присланный сервером код страницы
    html_code = page.get_page_source()
    assert 'users' not in html_code

    # Проверить вывод сообщения о блокировке запроса
    assert 'Ваш запрос был отклонен из соображений безопасности.' in page.security_error.get_text()

    print('SQL-injection is blocked')
