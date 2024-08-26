from random import randrange, uniform

from pydantic import BaseModel
from passlib.context import CryptContext

from constants import (
    USER_NAMES, SERVER_DOMAINS, COUNTRY_DOMAINS,
    AVAILABLE_PASSWORD_SYMBOLS
)


def generate_email() -> str:
    return (''.join(chr(randrange(97, 122 + 1)) for _ in range(2, randrange(3, 8 + 1))) +
            '@' + SERVER_DOMAINS[randrange(0, len(SERVER_DOMAINS))] +
            '.' + COUNTRY_DOMAINS[randrange(0, len(COUNTRY_DOMAINS))])


def generate_password() -> str:
    return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(
        ''.join(AVAILABLE_PASSWORD_SYMBOLS[randrange(0, len(AVAILABLE_PASSWORD_SYMBOLS))]
                for _ in range(8, 20)), salt="a" * 21 + "e"
    )


def generate_name() -> str:
    return USER_NAMES[randrange(0, len(USER_NAMES))]


def generate_age() -> int:
    return randrange(1, 36 + 1)


def generate_height() -> float:
    return uniform(145.0, 2000.0)


class User(BaseModel):
    email: str
    password: str
    name: str
    age: int
    height: float

    @staticmethod
    def generate_user() -> 'User':
        return User(
            email=generate_email(),
            password=generate_password(),
            name=generate_name(),
            age=generate_age(),
            height=generate_height()
        )


db = {
    'users': [User.generate_user() for _ in range(15)]
}