# Сумма чисел 2

"""
На вход программе подается натуральное число n.
 Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно) квадрат которых оканчивается на 2,5 или 8.
"""

"""
num = int(input())

total = 0
for i in range(num + 1):
    if (i ** i % 10 == 2) or (i ** i % 10 == 5) or (i ** i % 10 == 8):
        total += i
print(total)
"""

total = 0
for i in range(int(input()) + 1):
    if (pow(i, 2) % 10) in {2, 5, 8}:
        total += i
print(total)
