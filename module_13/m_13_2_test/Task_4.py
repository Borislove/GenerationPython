# Сумма цифр
"""
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
"""


# объявление функции
def print_digit_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    print(total)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
