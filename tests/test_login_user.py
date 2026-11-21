import pytest
import allure
from user_methods import UserMethods
from data import ResponseMessages


@allure.feature("Логин пользователя (POST /api/auth/login)")
class TestLoginUser:

    @allure.title("Успешный вход под существующим пользователем")
    def test_login_existing_user_returns_success_true(self, registered_user):
        login_payload = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }

        response = UserMethods.login_user(login_payload)
        body = response.json()

        assert (
            response.status_code == 200
            and body.get("success") is True
            and "accessToken" in body
            and body.get("user", {}).get("email") == registered_user["email"]
        )

    @allure.title("Ошибка входа при передаче неверного логина и/или пароля")
    @pytest.mark.parametrize(
        "wrong_fields",
        [
            ["email"],
            ["password"],
            ["email", "password"]
        ]
    )
    def test_login_with_wrong_credentials_returns_401_error(self, registered_user, wrong_fields):
        login_payload = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
        for field in wrong_fields:
            login_payload[field] = f"wrong_{login_payload[field]}"

        response = UserMethods.login_user(login_payload)
        body = response.json()

        assert (
            response.status_code == 401
            and body.get("success") is False
            and body.get("message") == ResponseMessages.INCORRECT_CREDENTIALS
        )
