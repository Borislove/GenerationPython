# Обратный порядок 2
"""
Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
"""

#reverse number
num = int(input())
last_digit = 0

while num != 0:
    last_digit = num % 10
    num //= 10
    print(str(last_digit) + "", end='')

"""test
5086334
4336805
"""

"""
num = int(input())
while num:
    print(num % 10, end='')
    num //= 10
"""