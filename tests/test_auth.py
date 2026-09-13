import allure


@allure.feature("Авторизация")
class TestAuthorization:
    @allure.title("Вход в систему с валидными данными")
    def test_successful_login(self, registered_user, login_page, main_page):
        login_page.open()
        login_page.login(registered_user["username"], registered_user["password"])
        login_page.wait_for_redirect_to_main()

        assert main_page.is_authorized()

    @allure.title("Проверка обязательности полей при авторизации")
    def test_login_fields_required(self, login_page):
        login_page.open()
        login_page.fill_username("testuser")

        assert login_page.is_login_button_disabled()

    @allure.title("Авторизация с неверным паролем")
    def test_login_with_invalid_password(self, registered_user, login_page):
        login_page.open()
        login_page.login(registered_user["username"], "WrongPassword123")

        assert login_page.is_opened()

    @allure.title("Переход на страницу регистрации со страницы авторизации")
    def test_redirect_to_register_from_login(self, login_page, register_page):
        login_page.open()
        login_page.click_signup()

        assert register_page.is_form_visible()