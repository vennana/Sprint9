from data.test_data import TestData
import allure


@allure.feature("Регистрация")
class TestAccount:
    @allure.title("Создание аккаунта с валидными данными")
    def test_successful_account_creation(self, register_page, login_page):
        user = TestData.get_new_user()
        register_page.open()
        register_page.register(user)
        # ИСПРАВЛЕНО: ждём редиректа перед проверкой.
        register_page.wait_for_redirect_to_login()

        assert login_page.is_opened()

    @allure.title("Проверка обязательности полей при регистрации")
    def test_registration_fields_required(self, register_page):
        register_page.open()
        register_page.fill_first_name("Test")
        register_page.fill_last_name("User")
        register_page.fill_email("test@example.com")
        register_page.fill_password("Test123456")

        assert register_page.is_register_button_disabled()

    @allure.title("Переход на страницу авторизации со страницы регистрации")
    def test_redirect_to_login_from_register(self, register_page, login_page):
        register_page.open()
        register_page.click_login()

        assert login_page.is_opened()