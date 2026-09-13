import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from data.test_data import TestData
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.recipe_create_page import RecipeCreatePage
from pages.register_page import RegisterPage


@pytest.fixture
def driver():
    selenoid_url = os.getenv("SELENOID_URL")

    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.set_capability("browserName", "chrome")

    if selenoid_url:
        options.add_argument("--headless")
        browser = webdriver.Remote(
            command_executor=selenoid_url,
            options=options,
        )
    else:
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)

    yield browser
    browser.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def register_page(driver):
    return RegisterPage(driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def recipe_create_page(driver):
    return RecipeCreatePage(driver)


@pytest.fixture
def registered_user(register_page):
    user = TestData.get_new_user()
    register_page.open()
    register_page.register(user)
    register_page.wait_for_redirect_to_login()
    return user


@pytest.fixture
def authenticated_user(registered_user, login_page):
    login_page.open()
    login_page.login(registered_user["username"], registered_user["password"])
    login_page.wait_for_redirect_to_main()
    return registered_user