### Класс APIRouter

Данный класс нужен для того, чтобы сгруппировать контроллеры, выполняющие схожие функции в системе.

Например: 
- Роутер авторизации
    - Контроллер регистрации
    - Контроллер аутентификации
    - Контроллер выхода из аккаунта

- Роутер обработки заказов
    - Контроллер чтения информации о заказе
    - Контроллер удаления заказа
    - и т.д.

<br>

Основные аргументы конструктора класса APIRouter(...):

| Аргумент | Тип | Для чего нужен |
|----------|-----|----------------|
prefix|str|- Задает общий prefix для соответствующих контроллеров|
tags|List[str, Enum]|- Добавляет разделы в OpenAPI и ReDoc документацию <br><br>- Если в роутере не будут указаны теги, то в документации информация о контроллерах сгруппированна не будет<br><br>- Если будет несколько разных тегов, то информация о контроллерах будет дублироваться
...|...|In process

<br>

Особенности Path-параметров пути:

- Данные параметры мы указываем в фигурных скобках в пути контроллера

- Их мы должны продублировать в функции-контроллере, еслихотим обратиться к ним. **`Ошибаться в названии нельзя!`**

- Если мы хотим, чтобы Path-параметр был определенного типа, мы должны сделать аннотацию типа соответствующего параметра функции

    - Иначе по дефолту все Path-параметры будут восприниматься как строки

    - При передачи некорректного параметра (при том, что указана аннотация типа), будет возникать ошибка `422`

    - Корректность параметров проверяет библиотека Pydantic

    ```python
        @vehicle_router.get('/{vehicle_id}/')
        async def get_vehicle_by_id(vehicle_id: int):
            return f'Vehicle with id: {vehicle_id}'
    ```

<br>

Особенность порядка следования контроллерова в файле:

- При обработке входящего http запроса, FastAPI начинает парсить контроллеры сверху-->вниз

- Фреймворк сравнивает url запроса с путями роутеров и контроллеров

- Важно располагать свои контроллеры в порядке от частного к общему сверху вниз для того, чтобы избежать ошибок вызова неверного контроллера

<br>

Пример неверного расположения контроллеров:

```python
@vehicle_router.get('/{vehicle_name}/')
async def get_vehicle_by_name(vehicle_name: str):
    return f'Vehicle with name: {vehicle_name}'


@vehicle_router.get('/my/')
async def get_my_vehicle():
    return 'My vehicle'
```

<br>

Пример корректно расположенных контроллеров:

```python
@vehicle_router.get('/my/')
async def get_my_vehicle():
    return 'My vehicle'


@vehicle_router.get('/{vehicle_name}/')
async def get_vehicle_by_name(vehicle_name: str):
    return f'Vehicle with name: {vehicle_name}'
```

<br>

Допустимые типы Path-параметров:

- Все базовые типы языка: str, int, float

- Перечисления Enum

<br>

Особенности Response-ов: Если у нас есть одна базовая Pydantic модель Vehicle и две вочерние модели Car и Ship, то из контроллера мы можем возвращать response как Vehicle, так и Car/Ship. Если контроллер у нас возвращает объект типа Car, а аннотация показывает, что будет возвращаться Vehicle, то часть атрибутов объекта будут скрыта. Но если контроллер возвращает объект типа vehicle, а аннотация показывает, что должен возвращаться любой дочерний объект, то У нас возникнет исключение!