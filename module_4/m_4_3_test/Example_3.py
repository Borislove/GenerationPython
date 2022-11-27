# Среднее число
"""
Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.

Формат входных данных
На вход программе подаётся три различных целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести среднее число.
"""

"""
num1, num2, num3 = int(input()), int(input()), int(input())
a, b, c = num1, num2, num3

if a < b < c or a > b > c:
    print(b)
elif c < a < b or c > a > b:
    print(a)
else:
    print(c)
"""

"""
if num3 < num1 < num2 or num2 < num1 < num3:
    print(num1)
elif num1 < num3 < num2 or num2 < num3 < num1:
    print(num3)
else:
    print(num2)
"""

lst = [int(input()) for _ in range(3)]
print(lst[0] + lst[1] + lst[2] - min(lst) - max(lst))

"""
from statistics import median
print(median([int(input()) for _ in range(3)]))
"""
