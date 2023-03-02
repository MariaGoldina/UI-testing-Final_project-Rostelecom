from Final_project.pages.base import WebPage
from Final_project.pages.elements import WebElement, ManyWebElements


auth_url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?response_type=code&scope=openid&client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Flk.rt.ru%252F&state=%7B%22uuid%22%3A%22BBD1B929-B623-4777-A0E8-E4965D3DBCCF%22%7D'

check_select_tab = 'rt-tab--active'
check_forgot_pass = 'login-form__forgot-pwd--animated'


class AuthPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = auth_url
        super().__init__(web_driver, url)

    title = WebElement(css_selector='.card-container__title')
    tabs = ManyWebElements(css_selector='.rt-tab')
    tab_phone = WebElement(id='t-btn-tab-phone')
    tab_email = WebElement(id='t-btn-tab-mail')
    tab_user_login = WebElement(id='t-btn-tab-login')
    tab_ls = WebElement(id='t-btn-tab-ls')
    input_login_field = WebElement(id='username')
    input_login_field_title = WebElement(css_selector='div.tabs-input-container__login>div>span.rt-input__placeholder')
    input_pass_field = WebElement(id='password')
    input_pass_field_title = WebElement(css_selector='div.rt-input--actions>span.rt-input__placeholder')
    log_in_btn = WebElement(name='login')
    checkbox_remember_me = WebElement(css_selector='.rt-checkbox')
    auth_error_message = WebElement(id='form-error-message')
    login_error_message = WebElement(css_selector='.rt-input-container__meta--error')
    forgot_pass = WebElement(id='forgot_password')
    registration_btn = WebElement(id='kc-register')
    user_name = WebElement(css_selector='h2.sc-bvFjSx')
    security_error = WebElement(css_selector="body>h2")
