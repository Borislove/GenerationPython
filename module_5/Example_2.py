# Шахматная доска

"""
Заданы две клетки шахматной доски. Напишите программу,
 которая определяет имеют ли указанные клетки один цвет или нет.
 Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""

num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
x1, y1, x2, y2 = num1, num2, num3, num4

#
line_1_input_1 = (x1 == 1 and y1 == 1) or (x1 == 1 and y1 == 3) or (x1 == 1 and y1 == 5) or (x1 == 1 and y1 == 7)
line_2_input_1 = (x1 == 2 and y1 == 2) or (x1 == 2 and y1 == 4) or (x1 == 2 and y1 == 6) or (x1 == 2 and y1 == 8)
line_3_input_1 = (x1 == 3 and y1 == 1) or (x1 == 3 and y1 == 3) or (x1 == 3 and y1 == 5) or (x1 == 3 and y1 == 7)
line_4_input_1 = (x1 == 4 and y1 == 2) or (x1 == 4 and y1 == 4) or (x1 == 4 and y1 == 6) or (x1 == 4 and y1 == 8)
line_5_input_1 = (x1 == 5 and y1 == 1) or (x1 == 5 and y1 == 3) or (x1 == 5 and y1 == 5) or (x1 == 5 and y1 == 7)
line_6_input_1 = (x1 == 6 and y1 == 2) or (x1 == 6 and y1 == 4) or (x1 == 6 and y1 == 6) or (x1 == 6 and y1 == 8)
line_7_input_1 = (x1 == 7 and y1 == 1) or (x1 == 7 and y1 == 3) or (x1 == 7 and y1 == 5) or (x1 == 7 and y1 == 7)
line_8_input_1 = (x1 == 8 and y1 == 2) or (x1 == 8 and y1 == 4) or (x1 == 8 and y1 == 6) or (x1 == 8 and y1 == 8)

input_1_passed = line_1_input_1 or line_2_input_1 or line_3_input_1 or line_4_input_1 or line_5_input_1 or line_6_input_1 or line_7_input_1 or line_8_input_1

# -----------------
line_1_input_2 = (x2 == 1 and y2 == 1) or (x2 == 1 and y2 == 3) or (x2 == 1 and y2 == 5) or (x2 == 1 and y2 == 7)
line_2_input_2 = (x2 == 2 and y2 == 2) or (x2 == 2 and y2 == 4) or (x2 == 2 and y2 == 6) or (x2 == 2 and y2 == 8)
line_3_input_2 = (x2 == 3 and y2 == 1) or (x2 == 3 and y2 == 3) or (x2 == 3 and y2 == 5) or (x2 == 3 and y2 == 7)
line_4_input_2 = (x2 == 4 and y2 == 2) or (x2 == 4 and y2 == 4) or (x2 == 4 and y2 == 6) or (x2 == 4 and y2 == 8)
line_5_input_2 = (x2 == 5 and y2 == 1) or (x2 == 5 and y2 == 3) or (x2 == 5 and y2 == 5) or (x2 == 5 and y2 == 7)
line_6_input_2 = (x2 == 6 and y2 == 2) or (x2 == 6 and y2 == 4) or (x2 == 6 and y2 == 6) or (x2 == 6 and y2 == 8)
line_7_input_2 = (x2 == 7 and y2 == 1) or (x2 == 7 and y2 == 3) or (x2 == 7 and y2 == 5) or (x2 == 7 and y2 == 7)
line_8_input_2 = (x2 == 8 and y2 == 2) or (x2 == 8 and y2 == 4) or (x2 == 8 and y2 == 6) or (x2 == 8 and y2 == 8)

input_2_passed = line_1_input_2 or line_2_input_2 or line_3_input_2 or line_4_input_2 or line_5_input_2 or line_6_input_2 or line_7_input_2 or line_8_input_2

# black
line_1_input_1_black = (x1 == 1 and y1 == 2) or (x1 == 1 and y1 == 4) or (x1 == 1 and y1 == 6) or (x1 == 1 and y1 == 8)
line_2_input_1_black = (x1 == 2 and y1 == 1) or (x1 == 2 and y1 == 3) or (x1 == 2 and y1 == 5) or (x1 == 2 and y1 == 7)
line_3_input_1_black = (x1 == 3 and y1 == 2) or (x1 == 3 and y1 == 4) or (x1 == 3 and y1 == 6) or (x1 == 3 and y1 == 8)
line_4_input_1_black = (x1 == 4 and y1 == 1) or (x1 == 4 and y1 == 3) or (x1 == 4 and y1 == 5) or (x1 == 4 and y1 == 7)
line_5_input_1_black = (x1 == 5 and y1 == 2) or (x1 == 5 and y1 == 4) or (x1 == 5 and y1 == 6) or (x1 == 5 and y1 == 8)
line_6_input_1_black = (x1 == 6 and y1 == 1) or (x1 == 6 and y1 == 3) or (x1 == 6 and y1 == 5) or (x1 == 6 and y1 == 7)
line_7_input_1_black = (x1 == 7 and y1 == 2) or (x1 == 7 and y1 == 4) or (x1 == 7 and y1 == 6) or (x1 == 7 and y1 == 8)
line_8_input_1_black = (x1 == 8 and y1 == 1) or (x1 == 8 and y1 == 3) or (x1 == 8 and y1 == 5) or (x1 == 8 and y1 == 7)

input_1_passed_black = line_1_input_1_black or line_2_input_1_black or line_3_input_1_black or line_4_input_1_black or line_5_input_1_black or line_6_input_1_black or line_7_input_1_black or line_8_input_1_black

line_1_input_2_black = (x2 == 1 and y2 == 2) or (x2 == 1 and y2 == 4) or (x2 == 1 and y2 == 6) or (x2 == 1 and y2 == 8)
line_2_input_2_black = (x2 == 2 and y2 == 1) or (x2 == 2 and y2 == 3) or (x2 == 2 and y2 == 5) or (x2 == 2 and y2 == 7)
line_3_input_2_black = (x2 == 3 and y2 == 2) or (x2 == 3 and y2 == 4) or (x2 == 3 and y2 == 6) or (x2 == 3 and y2 == 8)
line_4_input_2_black = (x2 == 4 and y2 == 1) or (x2 == 4 and y2 == 3) or (x2 == 4 and y2 == 5) or (x2 == 4 and y2 == 7)
line_5_input_2_black = (x2 == 5 and y2 == 2) or (x2 == 5 and y2 == 4) or (x2 == 5 and y2 == 6) or (x2 == 5 and y2 == 8)
line_6_input_2_black = (x2 == 6 and y2 == 1) or (x2 == 6 and y2 == 3) or (x2 == 6 and y2 == 5) or (x2 == 6 and y2 == 7)
line_7_input_2_black = (x2 == 7 and y2 == 2) or (x2 == 7 and y2 == 4) or (x2 == 7 and y2 == 6) or (x2 == 7 and y2 == 8)
line_8_input_2_black = (x2 == 8 and y2 == 1) or (x2 == 8 and y2 == 3) or (x2 == 8 and y2 == 5) or (x2 == 8 and y2 == 7)
input_2_passed_black = line_1_input_2_black or line_2_input_2_black or line_3_input_2_black or line_4_input_2_black or line_5_input_2_black or line_6_input_2_black or line_7_input_2_black or line_8_input_2_black

if (input_1_passed and input_2_passed) or (input_1_passed_black and input_2_passed_black):
    print('YES')
else:
    print('NO')
