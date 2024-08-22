from typing import List, Union

from fastapi import APIRouter, Depends

from models import User, Order, TestModel
from services import UserService
from dependencies import get_user_service, get_order_service

user_router = APIRouter(prefix='/users', tags=['users'])

order_router = APIRouter(prefix='/orders', tags=['orders'])


@user_router.get('/smth/{smth_id}')
async def test_params(smth_id: str | None = 'test', q: int | None = 3) -> str:
    return f'Something... {smth_id} - {q}'


@user_router.post('/test_params/{path}')
async def test_different_params_types(
    body: TestModel,
    q: Union[int, None],
    path: float,
    user_service: UserService = Depends(get_user_service)
) -> str:
    return f'Path parameter: {path}     ' \
            f'Query parameter: {q}      ' \
            f'Request body: {body}      '


@user_router.get('/')
async def get_all_users(
    per_page: Union[int, None] = None,
    page: int | None = None,
    is_adult: bool | None = None,
    user_service: UserService = Depends(get_user_service)
) -> List[User]:
    response = user_service.get_all_users(per_page, page, is_adult)
    return response