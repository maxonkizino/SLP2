import ast


def func(data):
    try:
        if isinstance(int(data),int):
            print("Введено число")
            strok = str(data)
            print("Колличество разрядов")
            return len(strok)
    except Exception as e:
        try:
            coll=ast.literal_eval(data)
            if isinstance(coll, list):
                print("Введен список")
                try:
                    while 1:
                        coll.remove(0)
                except Exception as e2:
                    pos = [i for i in coll if i>0]
                    try:
                        prod=pos[0]*pos[1]
                        print("Произведение 2 первых положительных чисел равно",prod)
                        return prod
                    except Exception as e3:
                        return "Недостаточно положительных элементов"

            elif isinstance(coll, dict):
                print("Введен словарь")
                if len(coll)>=3:
                     sorted_keys = sorted(coll, key=coll.get)
                     print("Первые 3 минимальные элементы")
                     return sorted_keys[:3]
                else:
                    return "В словаре недостаточно элементов\n"
        except Exception as e5:
                print("Введена строка")
                char_dict = {}
                for i in data:
                    char_dict[i]=data.count(i)
                print("Список с колличеством вхождений букв")
                return char_dict
    finally:
        print("Завершение работы функции.")

data=input("Введите данные\n")
b=func(data)
print(b)

