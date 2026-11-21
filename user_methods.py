import requests
import allure
from data import Urls


class UserMethods:

    @staticmethod
    @allure.step("Отправить POST-запрос на регистрацию пользователя")
    def register_user(payload):
        return requests.post(Urls.REGISTER_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Отправить POST-запрос на авторизацию пользователя")
    def login_user(payload):
        return requests.post(Urls.LOGIN_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Отправить DELETE-запрос на удаление пользователя")
    def delete_user(access_token):
        return requests.delete(
            Urls.USER_ENDPOINT,
            headers={"Authorization": access_token}
        )
