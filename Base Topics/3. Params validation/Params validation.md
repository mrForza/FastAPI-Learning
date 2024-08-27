### Валидация Query и Path параметров


Annotated - это класс из модуля typing, который нужен для того, чтобы задать дополнительные метаданные определенному типу

```python
import sys
from typing import Annotated, get_type_hints


a: Annotated[str, 'Metadat1', 'Lorem ipsum'] = 'test_value'
x: int = 3

print(get_type_hints(sys.modules[__name__]))  # Выводит подсказки типов
print(get_type_hints(sys.modules[__name__], include_extras=True))  # Выводит подсказкри типов вместе с метаданными
print(get_type_hints(sys.modules[__name__], include_extras=True).get('a').__metadata__)  # Выводит только метаданные
```

<br>

Для того, чтобы задать дополнительные метаданные любым параметрам в контроллере, нужно в Annotated передать сответствующий класс параметра:
Query, Path, Body и т.д.

Пример:
```python
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
    ),] = 'af08b478ac'
) -> str:
    return f'{query_param}'
```


**Важные параметры конструкторов дочерних классов класса Params:**
- `title` - Удобочитаемое название параметра в документации
- `description` - Удобочитаемое описание параметра в документации
- `alias` - Алиас для параметра, если он нарушает правила языка python
- `default` - Значение по-умолчанию `НЕ ИСПОЛЬЗУЕТСЯ В НОВЫХ ВЕРСИЯХ!`
- `examples` - Примеры разрешенных значений для документации
- `deprecated` - Памятка, что параметр больше не используется, для документации
- `include_in_schema` - Включать ли подробное описание в документацию
- `min_length` - Минимальная длина строкового параметра
- `max_length` - Максимальная длина строкового параметра
- `pattern` - Регулярное выражение для строкового параметра
- `gt` - Числовое значение (int, float) должно быть меньше чем
- `lt` - Числовое значение (int, float) должно быть больше чем
- `ge` - Числовое значение (int, float) должно быть меньше или равно чем
- `le` - Числовое значение (int, float) должно быть больше или равно чем
- `allow_inf_nan` -  Числовое значение float может принимать значения +inf, -inf и nan