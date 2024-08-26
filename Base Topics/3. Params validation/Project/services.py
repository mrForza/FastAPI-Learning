from typing import List

from models import User, db


class UserNotFound(Exception):
    @property
    def message(self) -> str:
        return 'User not found'


class UserService:
    def get_user_by_email(self, email: str) -> User:
        for user in db.get('users', []):
            if user.email == email:
                return user
        raise UserNotFound()


    def get_all_users(self) -> List[User]:
        return db.get('users', [])


    def create_user(self):
        pass


    @staticmethod
    def get_service() -> 'UserService':
        return UserService()
