# Наибольшее и наименьшее
# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.

"""
num1, num2, num3, num4, num5 = int(input()), int(input()), int(input()), int(input()), int(input())

min_number = min(num1, num2, num3, num4, num5)
max_number = max(num1, num2, num3, num4, num5)

print('Наименьшее число =', min_number)
print('Наибольшее число =', max_number)
"""

lst = [int(input()) for _ in range(5)]
print('Наименьшее число =', min(lst))
print('Наибольшее число =', max(lst))
