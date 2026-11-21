import random
import string
import allure
from faker import Faker

fake = Faker()


def generate_random_string(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


@allure.step("Сгенерировать данные нового пользователя")
def generate_user_payload():
    return {
        "email": f"{fake.user_name()}_{generate_random_string()}@yandex.ru",
        "password": fake.password(length=10, special_chars=False),
        "name": fake.first_name()
    }
