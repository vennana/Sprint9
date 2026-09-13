from data.test_data import TestData
from pages.base_page import BasePage
from pages.locators import MainLocators


class MainPage(BasePage):
    def open(self):
        self.open_url(TestData.RECIPES_URL)
        return self

    def click_create_recipe(self):
        self.click(MainLocators.CREATE_RECIPE)

    def is_authorized(self):
        return self.is_url_contains("/recipes") and self.is_visible(MainLocators.LOGOUT_BUTTON)