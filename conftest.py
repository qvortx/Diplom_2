import pytest
import allure
from helpers import generate_user_payload
from user_methods import UserMethods
from order_methods import OrderMethods


@pytest.fixture
def registered_user():
    """
    Создаёт пользователя перед тестом, возвращает его данные с access_token
    и удаляет пользователя после завершения теста.
    """
    user_data = generate_user_payload()
    response = UserMethods.register_user(user_data)
    access_token = response.json().get("accessToken")

    yield {
        **user_data,
        "access_token": access_token
    }

    with allure.step("Пост-условие (Teardown): удалить тестового пользователя"):
        if access_token:
            UserMethods.delete_user(access_token)


@pytest.fixture
def new_user_payload():
    """
    Генерирует словарь данных для регистрации нового пользователя,
    а после завершения теста удаляет созданного пользователя.
    """
    payload = generate_user_payload()

    yield payload

    with allure.step("Пост-условие (Teardown): удалить созданного в тесте пользователя"):
        login_response = UserMethods.login_user({
            "email": payload["email"],
            "password": payload["password"]
        })
        access_token = login_response.json().get("accessToken")
        if access_token:
            UserMethods.delete_user(access_token)


@pytest.fixture
def valid_ingredients():
    """
    Получает актуальные идентификаторы ингредиентов для создания заказа.
    """
    response = OrderMethods.get_ingredients()
    ingredients = response.json().get("data", [])
    return [ingredients[0]["_id"], ingredients[1]["_id"]]
