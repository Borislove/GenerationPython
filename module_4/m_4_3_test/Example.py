# Гонка спидстеров

"""
Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара.
В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир, поэтому Флэш решил не рисковать без причины,
и узнать у своего друга Циско Рамона есть ли смысл принимать вызов. Циско получил данные, что скорость Зума равна n,
а скорость Флэша равна k.

Напишите программу, которая должна вывести ответ Циско на вопрос Флэша.

Формат входных данных
На вход программе подаётся два целых числа n и k, скорость Зума и Флэша.

Формат выходных данных
Если Зум быстрее Флэша нужно вывести «NO», если Флэш быстрее Зума нужно вывести «YES», если их скорости равны нужно вывести "Don't know".
"""

"""
num1, num2, = int(input()), int(input())

speed_zoom = num1
speed_flash = num2

if speed_zoom > speed_flash:
    print('NO')
elif speed_zoom < speed_flash:
    print('YES')
else:
    print("Don't know")
"""

# v1.1
speed_zoom, speed_flash = int(input()), int(input())
if speed_zoom > speed_flash:
    print('NO')
elif speed_zoom < speed_flash:
    print('YES')
else:
    print("Don't know")

""" ???
zum, flash, answer = int(input()), int(input()), ("Don't know", "NO", "YES")
print(answer[0 if zum == flash else[1,2][zum < flash]])
"""
