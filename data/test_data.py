from faker import Faker
from pathlib import Path

fake = Faker()

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"


class TestData:
    BASE_URL = "https://foodgram-frontend-1.foodgram.education-services.ru"
    SIGNIN_URL = f"{BASE_URL}/signin"
    SIGNUP_URL = f"{BASE_URL}/signup"
    RECIPES_URL = f"{BASE_URL}/recipes"
    RECIPE_CREATE_URL = f"{BASE_URL}/recipes/create"

    PASSWORD = "Test123456!"

    @staticmethod
    def get_new_user():
        return {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "username": fake.user_name() + str(fake.random_int(min=1000, max=9999)),
            "email": fake.email(),
            "password": TestData.PASSWORD,
        }

    @staticmethod
    def get_recipe_data():
        return {
            "name": f"Тестовый рецепт {fake.random_int(min=1000, max=9999)}",
            "ingredient": "помидор",
            "ingredient_amount": "250",
            "cooking_time": "30",
            "description": "Тестовый рецепт для проверки создания.",
            "image": str(ASSETS_DIR / "test_image.png"),
        }