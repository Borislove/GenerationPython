# Делители-1 🌶️
"""
На вход программе подается два натуральных числа a и b (a < a< b).
Напишите программу, которая находит натуральное число из отрезка [a; b] с максимальной суммой делителей.
"""

a, b = int(input()), int(input())
total = 0
max_total = 0
x = 0
for i in range(a, b + 1):
    for k in range(1, i + 1):
        if i % k == 0:
            total += k
    if total >= max_total:
        max_total = total
        x = i
    total = 0
print(x, max_total)
