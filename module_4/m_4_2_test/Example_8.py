# Ход короля 🌶️

"""
Даны две различные клетки шахматной доски. Напишите программу,
 которая определяет, может ли король попасть с первой клетки на вторую одним ходом.
  Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки,
  потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом короля можно попасть во вторую, или «NO» в противном случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.
"""

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())


"""
num1 = 1
num2 = 8
num3 = 8
num4 = 1

ceil_1 = (1 <= num1 <= 8) and (1 <= num2 <= 8)
ceil_2 = (1 <= num3 <= 8) and (1 <= num4 <= 8)

correct_1 = num1 + 1 == num3
correct_2 = num2 + 1 == num4
correct_passed = correct_1 and correct_2

column_test = num1 == num3 - 1  # or num1 > num3 - 1  # столбец
line_test = num2 == num4 - 1  # строка

vertical_position_up_right = (num2 > num4) and (num1 < num3)
vertical_position_down_right = (num4 > num2) and (num1 < num3)

vertical_position_up_left = (num2 > num4) and (num1 > num3)
vertical_position_down_left = (num4 > num2) and (num1 > num3)

position_passed = vertical_position_up_right \
                  or vertical_position_down_right \
                  or vertical_position_up_left \
                  or vertical_position_down_left

# column , line?
if  (position_passed) and (ceil_1 and ceil_2) :
    print('YES')
else:
    print('NO')


print('ceil_1', ceil_1)
print('ceil_2', ceil_2)
"""

lst = [int(input()) for _ in range(4)]
print('YES' if -1 <= lst[0] - lst[2] <= 1 and -1 <= lst[1] - lst[3] <= 1 else 'NO')
