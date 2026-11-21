class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"
    REGISTER_ENDPOINT = f"{BASE_URL}/api/auth/register"
    LOGIN_ENDPOINT = f"{BASE_URL}/api/auth/login"
    USER_ENDPOINT = f"{BASE_URL}/api/auth/user"
    INGREDIENTS_ENDPOINT = f"{BASE_URL}/api/ingredients"
    ORDERS_ENDPOINT = f"{BASE_URL}/api/orders"


class ResponseMessages:
    USER_ALREADY_EXISTS = "User already exists"
    REQUIRED_FIELDS_ERROR = "Email, password and name are required fields"
    INCORRECT_CREDENTIALS = "email or password are incorrect"
    INGREDIENTS_REQUIRED = "Ingredient ids must be provided"


class OrderData:
    INVALID_INGREDIENT_HASH = ["invalid_hash_12345"]
