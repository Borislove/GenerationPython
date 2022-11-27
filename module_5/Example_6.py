# Ход слона 🌶️
"""
Даны две различные клетки шахматной доски.
Напишите программу, которая определяет, может ли слон попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
Программа должна вывести «YES», если из первой клетки ходом слона можно попасть во вторую или «NO» в противном случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный слон ходит по диагоналям.
"""

"""
# что за дичь! почему не работает 28 тест?
num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
x1, y1, x2, y2 = num1, num2, num3, num4

# column test
column_test = x1 != x2
# column test
line_test = y1 != y2

vertical_left_up = (x2 < x1) and (y2 < y1)
vertical_right_up = (x2 > x1) and (y2 < y1)
vertical_left_down = (x2 < x1) and (y2 > y1)
vertical_right_down = (x2 > x1) and (y2 > y1)

test_1 = (x1 + y1) % 2 == 0
test_2 = (x2 + y2) % 2 == 0

if (column_test and line_test) and (
        vertical_left_up or vertical_right_up or vertical_left_down or vertical_right_down) and (test_1 or test_2):
    print('YES')
else:
    print('NO')

ceil_1 = (1 <= num1 <= 8) and (1 <= num2 <= 8)
ceil_2 = (1 <= num3 <= 8) and (1 <= num4 <= 8)
"""

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
    print('YES')
else:
    print('NO')
