# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# print('Проверка истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат')

#Идеальное рещение
for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)
# claim_1 = False
# claim_2 = False
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             claim_1 = not (bool(x) or bool(y) or bool(z))
#             claim_2 = not bool(x) and not bool(y) and not bool(z)
#             print(f'При значении предикат X, Y, Z = [{bool(x)}, {bool(y)}, {bool(z)}]', end=', ')
#             print(f'утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z = {claim_1 == claim_2}')

# def TruthCheck ():
#     result = True
#     for n in range(0, 8):
#         num = bin(n)
#         print(f'{n} =', end=" ") # Нумерация
#         print(f'{num} =', end=" ") # Бинарное представление числа
#         num = num.replace('b', '0')
#         X = int(num[-3])
#         Y = int(num[-2])
#         Z = int(num[-1])
#         print(f'{X}{Y}{Z}', end=" ") # Результат сортировки нужных значений xyz
#         result = (not(X or Y or Z)) == ((not X) and (not Y) and (not Z))
#         print()
#         if result is True:
#             result = "Утверждение является истинным"
#         else:
#             result = "Утверждение является ложным"
#     return result
# print(TruthCheck())

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


# 1.
# x = int(input('Введите число x '))
# y = int(input('Введите число y '))
# z = int(input('Введите число z '))

# a = x * y * z
# b = x + y + z

# if a > 0:
#     a = 0
# elif a < 1:
#     a = 1
# if b > 0:
#     b = 1
# elif b < 1:
#     b = 1

# if a == b:
#     print('Утверждение истинно')
# elif a != b:
#     print('Утверждение ложно')

# leftSide = not (x or y or z)
# rightSide = not x and not y and not z
# result = leftSide == rightSide

# if result == True:
#     print('Утверждение истинно')
# else:
#     print('Утверждение ложно')