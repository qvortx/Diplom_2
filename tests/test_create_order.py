import allure
from order_methods import OrderMethods
from data import OrderData, ResponseMessages


@allure.feature("Создание заказа (POST /api/orders)")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и валидными ингредиентами")
    def test_create_order_with_auth_and_ingredients_returns_success(
        self, registered_user, valid_ingredients
    ):
        payload = {"ingredients": valid_ingredients}

        response = OrderMethods.create_order(
            payload,
            access_token=registered_user["access_token"]
        )
        body = response.json()

        assert (
            response.status_code == 200
            and body.get("success") is True
            and isinstance(body.get("order", {}).get("number"), int)
        )

    @allure.title("Создание заказа без авторизации с валидными ингредиентами")
    def test_create_order_without_auth_and_with_ingredients_returns_success(
        self, valid_ingredients
    ):
        payload = {"ingredients": valid_ingredients}

        response = OrderMethods.create_order(payload)
        body = response.json()

        assert (
            response.status_code == 200
            and body.get("success") is True
            and isinstance(body.get("order", {}).get("number"), int)
        )

    @allure.title("Ошибка при создании заказа без ингредиентов")
    def test_create_order_without_ingredients_returns_400_error(self, registered_user):
        payload = {"ingredients": []}

        response = OrderMethods.create_order(
            payload,
            access_token=registered_user["access_token"]
        )
        body = response.json()

        assert (
            response.status_code == 400
            and body.get("success") is False
            and body.get("message") == ResponseMessages.INGREDIENTS_REQUIRED
        )

    @allure.title("Ошибка 500 при создании заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash_returns_500_error(self, registered_user):
        payload = {"ingredients": OrderData.INVALID_INGREDIENT_HASH}

        response = OrderMethods.create_order(
            payload,
            access_token=registered_user["access_token"]
        )

        assert (
            response.status_code == 500
            and "Internal Server Error" in response.text
        )
