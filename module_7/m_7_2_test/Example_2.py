# Последовательность чисел 2 🌶️

"""
Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания
m<n, или в порядке убывания в противном случае.

"""

m, n = int(input()), int(input())

"""
if m > n:
    for i in range(m, n - 1, -1):
        print(i)
elif m < n:
    for i in range(m, n + 1):
        print(i)
else:
    print(m)
"""

"""
if m > n:
    print('test')
else:
    print('no')
"""

if m < n:
    [print(i) for i in range(m, n + 1)]
else:
    [print(i) for i in range(m, n - 1, -1)]
