from data.test_data import TestData
from pages.base_page import BasePage
from pages.locators import RegisterLocators


class RegisterPage(BasePage):
    def open(self):
        self.open_url(TestData.SIGNUP_URL)
        return self

    def register(self, user):
        self.input_text(RegisterLocators.FIRST_NAME, user["first_name"])
        self.input_text(RegisterLocators.LAST_NAME, user["last_name"])
        self.input_text(RegisterLocators.USERNAME, user["username"])
        self.input_text(RegisterLocators.EMAIL, user["email"])
        self.input_text(RegisterLocators.PASSWORD, user["password"])
        self.click(RegisterLocators.REGISTER_BUTTON)

    def fill_first_name(self, value):
        self.input_text(RegisterLocators.FIRST_NAME, value)

    def fill_last_name(self, value):
        self.input_text(RegisterLocators.LAST_NAME, value)

    def fill_email(self, value):
        self.input_text(RegisterLocators.EMAIL, value)

    def fill_password(self, value):
        self.input_text(RegisterLocators.PASSWORD, value)

    def is_form_visible(self):
        return self.is_visible(RegisterLocators.TITLE)

    def is_register_button_disabled(self):
        return self.is_disabled(RegisterLocators.REGISTER_BUTTON)

    def click_login(self):
        self.click(RegisterLocators.LOGIN_LINK)

    def wait_for_redirect_to_login(self):
        self.wait_for_url_contains("/signin")