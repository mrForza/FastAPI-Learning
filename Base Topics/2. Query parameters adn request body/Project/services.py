from typing import List, Union

from models import User, Order, db


class UserService:
    def get_all_users(self, per_page: Union[int, None], page: int | None, is_adult: bool | None) -> List[User]:
        sample = db.get('user')
        if per_page is not None and page is not None:
            sample = sample[(page - 1) * per_page: per_page * page]

        if is_adult is not None:
            if is_adult:
                sample = list(filter(lambda person: person.age >= 18, sample))
            else:
                sample = list(filter(lambda person: person.age < 18, sample))
        return sample


class OrderService:
    pass
