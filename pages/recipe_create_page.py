from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data.test_data import TestData
from pages.base_page import BasePage
from pages.locators import RecipeLocators


class RecipeCreatePage(BasePage):
    def open(self):
        self.open_url(TestData.RECIPE_CREATE_URL)
        return self

    def fill_name(self, name):
        self.input_text(RecipeLocators.NAME, name)

    def add_ingredient(self, name, amount):
        self.input_text(RecipeLocators.INGREDIENT, name)

        suggestion_locator = (
            By.XPATH,
            RecipeLocators.INGREDIENT_SUGGESTION_TEMPLATE.format(name=name),
        )
        suggestion = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(suggestion_locator)
        )
        suggestion.click()

        self.input_text(RecipeLocators.INGREDIENT_AMOUNT, amount)
        self.click(RecipeLocators.ADD_INGREDIENT)

    def fill_cooking_time(self, value):
        self.input_text(RecipeLocators.COOKING_TIME, value)

    def fill_description(self, value):
        self.input_text(RecipeLocators.DESCRIPTION, value)

    def upload_image(self, image_path):
        path = Path(image_path)
        self.find_element(RecipeLocators.IMAGE).send_keys(str(path))

    def create_recipe(self, recipe):
        self.fill_name(recipe["name"])
        self.add_ingredient(recipe["ingredient"], recipe["ingredient_amount"])
        self.fill_cooking_time(recipe["cooking_time"])
        self.fill_description(recipe["description"])
        self.upload_image(recipe["image"])
        self.click(RecipeLocators.SUBMIT)

    def is_submit_button_disabled(self):
        return self.is_disabled(RecipeLocators.SUBMIT)

    def is_ingredient_added(self):
        return len(self.find_elements(RecipeLocators.INGREDIENT_ITEM)) > 0

    def is_created_recipe_displayed(self, recipe_name):
        title = self.find_element(RecipeLocators.RECIPE_TITLE)
        return self.is_url_contains("/recipes/") and recipe_name in title.text

    def is_opened(self):
        return self.is_url_contains("/recipes/create")