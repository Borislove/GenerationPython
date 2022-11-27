# Неравенство треугольника

# Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.

"""
num1 = int(input())
num2 = int(input())
num3 = int(input())

side_a = num1
side_b = num2
side_c = num3

first_test = side_a < side_b + side_c
second_test = side_b < side_a + side_c
third_test = side_c < side_a + side_b

if first_test and second_test and third_test:
    print('YES')
else:
    print('NO')
"""

"""
# v2.0
lst = [int(input()) for _ in range(3)]
for _ in range(len(lst)):
    if lst[0] < lst[1] + lst[2] \
            and lst[1] < lst[0] + lst[2] \
            and lst[2] < lst[0] + lst[1]:
        print('YES')
        break
    else:
        print('NO')
        break
"""

"""
# v2.1
lst = [int(input()) for _ in range(3)]
for _ in range(len(lst)):
    if lst[0] - lst[1] < lst[2] < lst[0] + lst[1]:
        print('YES')
        break
    else:
        print('NO')
        break
"""

# v3.1
lst = [int(input()) for _ in range(3)]
print('YES' if lst[0] - lst[1] < lst[2] < lst[0] + lst[1] else 'NO')
