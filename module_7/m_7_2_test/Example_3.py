# Последовательность чисел 3 🌶️
"""
Даны два целых числа m и n (m > n). Напишите программу, которая выводит все нечетные числа от m до n включительно в порядке убывания.
"""

num1, num2 = int(input()), int(input())
m = num1
n = num2

value = 0
count = 0

"""
if m > n:
    for i in range(n, m + 1):
        value = i
        if (i % 2 != 0):
            print(value)
"""

if m > n:
    for k in range(m, n - 1, -1):
        if (k % 2 != 0):
            print(k)



