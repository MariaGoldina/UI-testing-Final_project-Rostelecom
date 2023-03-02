# These are tests for project https://b2c.passport.rt.ru Ростелеком ИТ.
# Module: Registration form.

# How to run:
#  1) Download driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     Choose command "Run pytest in test_registration.py" in upper menu Run

import time
import pytest

from Final_project.pages.reg_page import *
from Final_project.pages.auth_page import *


@pytest.mark.reg
def test_registration_btn_work(web_browser):
    page = AuthPage(web_browser)

    # Нажать на кнопку Зарегистрироваться
    assert page.registration_btn.is_clickable()
    page.registration_btn.click()

    # Проверить, что произошел редирект на форму Регистрации
    new_page_title = page.title.get_text()
    assert "Регистрация" in str(new_page_title)

    print('\n"Registration" button works')


@pytest.mark.reg
@pytest.mark.parametrize('text', ['Аб',
                                  'АбВ',
                                  'АбВгДеёЖзИ',
                                  'АбВгдЕёжзИйклМнопрСтуфхЦчшщЪЫ',
                                  'АбВгдЕёжзИйклМнопрСтуфхЦчшщЪЫЬ',
                                  'абвгдеёжзи',
                                  'АБВГДЕЁЖЗИ'
                                  ],
                         ids=['2 symbols',
                              '3 symbols',
                              '10 symbols',
                              '29 symbols',
                              '30 symbols',
                              'only lower symbols',
                              'only upper symbols'
                              ])
def test_name_field_and_lastname_field_with_valid_data(web_browser, text):
    page = RegistrationPage(web_browser)

    # Ввести в поле Имя и поле Фамилия валидные тестовые данные
    # Перевести курсор в поле Email или мобильный телефон
    assert page.input_name.is_clickable() and page.input_lastname.is_clickable()
    page.input_name.send_keys(text)
    page.input_lastname.send_keys(text)
    page.input_email_or_phone.click()

    # Проверить, что под полем Имя и под полем Фамилия не появляется сообщение об ошибке ввода
    if page.name_and_lastname_errors.is_visible():
        for error in page.name_and_lastname_errors:
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' not in error.text
    else:
        print('Error messages are not on page')

    print('Name and lastname fields get valid data')


@pytest.mark.reg
@pytest.mark.parametrize('text', ['Аб-',
                                  'Аб-Г',
                                  'АбВ-',
                                  'Абв-Г',
                                  'АбВгДеёЖзИ-ОпрСТуФхцЧ',
                                  'АбВгДеёЖзИЙкЛм-ОпрСТуФхцЧшщЪы',
                                  'АбВгДеёЖзИЙкЛмН-ОпрСТуФхцЧшщЪыЬ'
                                  ],
                         ids=['2-0 symbols',
                              '2-1 symbols',
                              '3-0 symbols',
                              '3-1 symbols',
                              '10-10 symbols',
                              '14-14 symbols',
                              '15-15 symbols'
                              ])
def test_name_field_and_lastname_field_with_dash(web_browser, text):
    page = RegistrationPage(web_browser)

    # Ввести в поле Имя и поле Фамилия валидные тестовые данные
    # Перевести курсор в поле Email или мобильный телефон
    assert page.input_name.is_clickable() and page.input_lastname.is_clickable()
    page.input_name.send_keys(text)
    page.input_lastname.send_keys(text)
    page.input_email_or_phone.click()

    # Проверить, что под полем Имя и под полем Фамилия не появляется сообщение об ошибке ввода
    if page.name_and_lastname_errors.is_visible():
        for error in page.name_and_lastname_errors:
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' not in error.text
    else:
        print('Error messages are not on page')

    print('Name and lastname fields get valid data')


@pytest.mark.reg
@pytest.mark.parametrize('text', ['AbCdEfgHiJ',
                                  '1234567890',
                                  '!@#$%^&*()[]',
                                  'А',
                                  'АбВгдЕёжзИйклМнопрСтуфхЦчшщЪЫЬэ'
                                  ],
                         ids=['latin',
                              'numbers',
                              'special symbols',
                              '1 symbol',
                              '31 symbol'
                              ])
def test_name_field_with_invalid_data(web_browser, text):
    page = RegistrationPage(web_browser)

    # Ввести в поле Имя и поле Фамилия невалидные тестовые данные
    # Перевести курсор в поле Email или мобильный телефон
    assert page.input_name.is_clickable()
    page.input_name.send_keys(text)
    page.input_email_or_phone.click()

    # Проверить, что под полем Имя и под полем Фамилия не появляется сообщение об ошибке ввода
    errors_text = []
    for error in page.name_and_lastname_errors:
        if error.is_displayed():
            errors_text.append(error.text)
    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' == errors_text[0]

    print("Name fields doesn't get invalid data")
