from typing import Annotated, Union

from fastapi import APIRouter, Depends, Query, Path
from fastapi.responses import JSONResponse

from services import UserService, UserNotFound
from models import User


user_router = APIRouter(prefix='/users', tags=['users'])


@user_router.get('/something/')
async def get_something(
    query_param: Annotated[str, Query(
        alias='qparam-alias',
        alias_priority=1,
        validation_alias='Validation-Alias-For-Query-Param',
        serialization_alias='Serialization-Alias-For-Query-Param',
        title='Query Parameter',
        description='A human-readable description for Query Parameter',
        min_length=8,
        max_length=64,
        pattern=r'[0-9a-f]+',
        strict=True,
        examples=['aaf009f3f4', 'bbcbcbcbcbcbca', '010101101001'],
        include_in_schema=True
    ),] = 'af08b478ac',
    query_int_param: Annotated[int, Query(
        alias='integer',
        title='Integer query parameter',
        description='A human-readable integer query parameter\'s description',
        gt=8,
        le=56,
        include_in_schema=True
    )] = 12,
    query_float_param: Annotated[float, Query(
        alias='float',
        title='Float query parameter',
        description='A human-readable float query parameter\'s description',
        gt=1.57,
        include_in_schema=True,
        allow_inf_nan=True
    )] = 3.14
) -> str:
    return f'{query_param}, {query_int_param}, {query_float_param}'


@user_router.get('/')
async def get_users(user_service: UserService = Depends(UserService.get_service)) -> JSONResponse:
    response = user_service.get_all_users()
    return JSONResponse(content=list(map(lambda user: user.model_dump(), response)), status_code=200)


@user_router.get('/{email}/')
async def get_user_by_email(
    email: Annotated[
        str,
        Path(
            title='Email address',
            description='An email address which user can use to register' \
                ' in system. This addres should be unique',
            min_length=6,
            max_length=64,
            regex=r'\S{1,60}@[a-z]{1,10}\.[a-z]{1,5}'
        )
    ],
    user_service: UserService = Depends(UserService.get_service)
) -> JSONResponse:
    try:
        response = user_service.get_user_by_email(email)
        return JSONResponse(content=response.model_dump(), status_code=200)
    except UserNotFound as error:
        return JSONResponse(content=error.message, status_code=404)


@user_router.post('/')
async def add_user():
    pass
