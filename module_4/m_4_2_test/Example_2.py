# Принадлежность 2
"""
Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанным промежуткам.

Формат входных данных
На вход программе подаётся целое число xx.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""

#  ++++-3..........7+++   --->x

num = int(input())

if num <= -3 or num >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')
