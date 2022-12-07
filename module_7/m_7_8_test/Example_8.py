# Звездный треугольник 🌶️🌶️
"""
Дано нечетное натуральное число n.
Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным n в соответствии с примером:
"""

"""
num = int(input())
for i in range(1, num):
    print('*' * i)
    for j in range(1, i):
        print('*')
"""

"""
elka
num = int(input())
for i in range(1, num):
    print('*' * i)
    for j in range(1, i):
        i += i
        for k in range(j, i):
            print('*' * k)
"""

num = int(input())
for i in range(1, num + 1):
    print('*' * min(i, num - i + 1))