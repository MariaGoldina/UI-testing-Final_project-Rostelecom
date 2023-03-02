from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Final_project.pages.base import WebPage
from Final_project.pages.elements import WebElement, ManyWebElements


auth_url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?response_type=code&scope=openid&client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Flk.rt.ru%252F&state=%7B%22uuid%22%3A%22BBD1B929-B623-4777-A0E8-E4965D3DBCCF%22%7D'


class RegistrationPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = auth_url
        super().__init__(web_driver, url)
        registration = WebDriverWait(web_driver, timeout=10).until(
               EC.presence_of_element_located((By.ID, 'kc-register')))
        registration.click()
        super().wait_page_loaded()

    input_name = WebElement(name='firstName')
    input_lastname = WebElement(name='lastName')
    name_and_lastname_errors = ManyWebElements(css_selector='div.name-container>div>span')
    region_list = WebElement(css_selector='.register-form__dropdown>div>div>input')
    input_email_or_phone = WebElement(id='address')
    input_pass = WebElement(id='password')
    input_pass_confirm = WebElement(id='password-confirm')
    register_btn = WebElement(xpath='//button[@name="register"]')
