from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_FIELD = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Войти')]")
    SIGNUP_LINK = (By.XPATH, "//a[contains(., 'Создать аккаунт')]")
    TITLE = (By.XPATH, "//h1[contains(., 'Войти на сайт')]")


class RegisterLocators:
    FIRST_NAME = (By.NAME, "first_name")
    LAST_NAME = (By.NAME, "last_name")
    USERNAME = (By.NAME, "username")
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(., 'Создать аккаунт')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(., 'Войти')]")
    TITLE = (By.XPATH, "//h1[contains(., 'Регистрация')]")


class MainLocators:
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(., 'Выход')]")
    CREATE_RECIPE = (By.XPATH, "//a[contains(., 'Создать рецепт')]")


class RecipeLocators:
    NAME = (By.XPATH, "//form//input[@type='text'][1]")
    INGREDIENT = (By.XPATH, "//input[contains(@class, 'ingredientsInput')]")
    INGREDIENT_AMOUNT = (By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]")
    ADD_INGREDIENT = (By.XPATH, "//div[contains(@class, 'ingredientAdd')]")
    COOKING_TIME = (By.XPATH, "//div[contains(@class, 'cookingTime')]//input")
    DESCRIPTION = (By.XPATH, "//textarea")
    IMAGE = (By.CSS_SELECTOR, "input[type='file']")
    SUBMIT = (By.XPATH, "//button[contains(., 'Создать рецепт')]")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'ingredientsAddedItem')]")
    RECIPE_TITLE = (By.XPATH, "//h1[contains(@class, 'styles_single-card__title')]")
    INGREDIENT_SUGGESTION_TEMPLATE = "//div[starts-with(text(), '{name}')]"