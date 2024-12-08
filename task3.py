import random

n=int(input("Введите количество строк\n"))
m=int(input("Введите количество столбцов\n"))
mass=[[random.randint(0, 100) for i in range(m)] for g in range(n)]

print("Матрица:")
for i in range(n):
    for g in range(m):
        print (mass[i][g],end=' ')
    print()

min=mass[0][0]
max=mass[0][0]
minind=[0,0]
maxind=[0,0]

for i in range(n):
    for g in range(m):
        if mass[i][g]<min:
            min=mass[i][g]
            minind=[i+1,g+1]
        if mass[i][g] > max:
            max = mass[i][g]
            maxind = [i+1,g+1]

print(f"Минимальный элемент {min} с индексами {minind[0]} и {minind[1]} ")
print(f"Максимальный элемент {max} с индексами {maxind[0]} и {maxind[1]} ")