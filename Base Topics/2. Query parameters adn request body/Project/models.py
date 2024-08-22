from random import randrange, uniform

from pydantic import BaseModel

from constants import *


class User(BaseModel):
    name: str
    age: int
    email: str

    @staticmethod
    def generate_user() -> 'User':
        return User(
            name=USER_NAMES[randrange(0, len(USER_NAMES))],
            age=randrange(1, 30),
            email=(''.join([chr(randrange(97, 122)) for _ in range(2, randrange(2, 8))]) + '@' +
                   SERVER_DOMAINS[randrange(0, len(SERVER_DOMAINS))] + '.' + 
                   COUNTRY_DOMAINS[randrange(0, len(COUNTRY_DOMAINS))])
        )


class Order(BaseModel):
    name: str
    weight: float

    @staticmethod
    def generate_order() -> 'Order':
        return Order(
            name=ORDER_NAMES[randrange(0, len(ORDER_NAMES))],
            weight=uniform(0.125, 22.0)
        )


class TestModel(BaseModel):
    value: str
    number: float


db = {
    'user': [User.generate_user() for _ in range(20)],
    'order': [Order.generate_order() for _ in range(30)],
    'user-orders': [(randrange(0, 20), randrange(0, 30)) for _ in range(15)]
}