import allure

from data.test_data import TestData


@allure.feature("Рецепты")
class TestRecipe:
    @allure.title("Создание рецепта авторизованным пользователем")
    def test_create_recipe(self, authenticated_user, recipe_create_page):
        recipe = TestData.get_recipe_data()
        recipe_create_page.open()
        recipe_create_page.create_recipe(recipe)

        assert recipe_create_page.is_created_recipe_displayed(recipe["name"])

    @allure.title("Переход к созданию рецепта через меню")
    def test_create_recipe_from_menu(self, authenticated_user, main_page, recipe_create_page):
        main_page.open()
        main_page.click_create_recipe()

        assert recipe_create_page.is_opened()

    @allure.title("Проверка обязательности полей при создании рецепта")
    def test_recipe_fields_required(self, authenticated_user, recipe_create_page):
        recipe_create_page.open()

        assert recipe_create_page.is_submit_button_disabled()

        recipe_create_page.fill_name("Тестовый рецепт")

        assert recipe_create_page.is_submit_button_disabled()

    @allure.title("Добавление ингредиента в рецепт")
    def test_add_ingredient_to_recipe(self, authenticated_user, recipe_create_page):
        recipe_create_page.open()

        recipe_create_page.add_ingredient("помидор", "250")

        assert recipe_create_page.is_ingredient_added()