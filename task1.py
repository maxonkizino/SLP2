def func(a, b):
    while b:
        a, b = b, a % b
    return a

a=int(input("Введите первое число\n"))
b=int(input("Введите второе число\n"))
c=func(a,b)
print(f"Наибольший общий делитель {a} и {b} равен {c}")
