x = int(input('Введите координату X '))
y = int(input('Введите координату Y '))

def chetvert(x,y):
    a = 4
    if x > 0 and y > 0:
        a = 1
    elif x < 0 and y > 0:
        a = 2
    elif x < 0 and y < 0:
        a = 3
    print(f"Точка находится в {a} четверти плоскости")

chetvert(x,y)
