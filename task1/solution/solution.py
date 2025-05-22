def strict(func):
    def wrapper(*args, **kwargs):
        # Получаем аннотации типов
        annotations = func.__annotations__

        # Получаем имена параметров функции
        param_names = func.__code__.co_varnames[:func.__code__.co_argcount]

        # Проверяем позиционные аргументы
        for i, arg in enumerate(args):
            if i < len(param_names):
                param_name = param_names[i]
                if param_name in annotations:
                    expected_type = annotations[param_name]
                    if not isinstance(arg, expected_type):
                        raise TypeError

        # Проверяем именованные аргументы
        for param_name, arg in kwargs.items():
            if param_name in annotations:
                expected_type = annotations[param_name]
                if not isinstance(arg, expected_type):
                    raise TypeError

        return func(*args, **kwargs)

    return wrapper


# Тест
@strict
def sum_two(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(sum_two(1, 2))  # 3
    try:
        sum_two(1, 2.4)  # TypeError
    except TypeError:
        print("TypeError raised correctly")
