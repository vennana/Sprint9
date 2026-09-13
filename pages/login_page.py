from data.test_data import TestData
from pages.base_page import BasePage
from pages.locators import LoginLocators


class LoginPage(BasePage):
    def open(self):
        self.open_url(TestData.SIGNIN_URL)
        return self

    # ИСПРАВЛЕНО: используется LOGIN_FIELD вместо EMAIL.
    # Поле с name="email" — это поле ввода username (особенность Foodgram).
    def login(self, username, password):
        self.input_text(LoginLocators.LOGIN_FIELD, username)
        self.input_text(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def fill_username(self, username):
        self.input_text(LoginLocators.LOGIN_FIELD, username)

    def fill_password(self, password):
        self.input_text(LoginLocators.PASSWORD, password)

    def is_form_visible(self):
        return self.is_visible(LoginLocators.TITLE)

    def is_login_button_disabled(self):
        return self.is_disabled(LoginLocators.LOGIN_BUTTON)

    def click_signup(self):
        self.click(LoginLocators.SIGNUP_LINK)

    def is_opened(self):
        return self.is_url_contains("/signin") and self.is_form_visible()

    def wait_for_redirect_to_main(self):
        self.wait_for_url_contains("/recipes")