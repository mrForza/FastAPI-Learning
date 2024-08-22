from services import UserService, OrderService


def get_user_service() -> UserService:
    return UserService()


def get_order_service() -> OrderService:
    return OrderService()
