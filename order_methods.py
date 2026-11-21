import requests
import allure
from data import Urls


class OrderMethods:

    @staticmethod
    @allure.step("Отправить GET-запрос на получение списка ингредиентов")
    def get_ingredients():
        return requests.get(Urls.INGREDIENTS_ENDPOINT)

    @staticmethod
    @allure.step("Отправить POST-запрос на создание заказа")
    def create_order(payload, access_token=None):
        headers = {"Authorization": access_token} if access_token else None
        return requests.post(Urls.ORDERS_ENDPOINT, json=payload, headers=headers)
