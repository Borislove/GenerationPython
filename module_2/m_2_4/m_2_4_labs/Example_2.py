# СУММА ТРЕХ ЧИСЕЛ
# Напишите программу, которая считывает три целых числа и выводит на экран их сумму. Каждое число записано в отдельной строке.

"""
number1 = int(input())
number2 = int(input())
number3 = int(input())

sum = number1 + number2 + number3
print(sum)
"""

# v2
# print(int(input()) + int(input()) + int(input()))

"""
# v3
total = 0
for _ in range(3):
    num = int(input())
    total += num
print(total)
"""

# v4
total = 0
for _ in range(3):
    total += int(input())
print(total)

"""
# v5
num1, num2, num3, = int(input()), int(input()), int(input())
print(num1 + num2 + num3)
"""

# v6.0
print(sum(int(input()) for _ in range(3)))
