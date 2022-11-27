# Только +
"""
Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

Формат входных данных
На вход программе подаются три целых числа.

Формат выходных данных
Программа должна вывести одно число – сумму положительных чисел.

Примечание. Если положительных чисел нет, то следует вывести 0.
"""

"""
num1 = int(input())
num2 = int(input())
num3 = int(input())

sum = 0

if num1 > 0 % 2:
    sum += num1
if num2 > 0 % 2:
    sum += num2
if num3 > 0 % 2:
    sum += num3

print(sum)
"""

# v2
total = 0
lst = [int(input()) for _ in range(3)]
for i in range(len(lst)):
    if lst[i] > 0:
        total += lst[i]
print(total)

# v2_1
total = 0
for i in range(3):
    num = int(input())
    if num > 0:
        total += num
print(total)
