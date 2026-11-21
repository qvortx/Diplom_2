import pytest
import allure
from user_methods import UserMethods
from helpers import generate_user_payload
from data import ResponseMessages


@allure.feature("Создание пользователя (POST /api/auth/register)")
class TestCreateUser:

    @allure.title("Успешное создание уникального пользователя")
    def test_create_unique_user_returns_success_true(self, new_user_payload):
        response = UserMethods.register_user(new_user_payload)
        body = response.json()

        assert (
            response.status_code == 200
            and body.get("success") is True
            and "accessToken" in body
            and body.get("user", {}).get("email") == new_user_payload["email"]
            and body.get("user", {}).get("name") == new_user_payload["name"]
        )

    @allure.title("Ошибка при создании пользователя, который уже зарегистрирован")
    def test_create_existing_user_returns_403_error(self, registered_user):
        payload = {
            "email": registered_user["email"],
            "password": registered_user["password"],
            "name": registered_user["name"]
        }

        response = UserMethods.register_user(payload)
        body = response.json()

        assert (
            response.status_code == 403
            and body.get("success") is False
            and body.get("message") == ResponseMessages.USER_ALREADY_EXISTS
        )

    @allure.title("Ошибка при создании пользователя без одного из обязательных полей ({missing_field})")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_required_field_returns_403_error(self, missing_field):
        payload = generate_user_payload()
        del payload[missing_field]

        response = UserMethods.register_user(payload)
        body = response.json()

        assert (
            response.status_code == 403
            and body.get("success") is False
            and body.get("message") == ResponseMessages.REQUIRED_FIELDS_ERROR
        )
