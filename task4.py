def func(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль невозможно!"
    finally:
        print("Завершение работы функции.")
print(func(10,0))
print(func(10,5))