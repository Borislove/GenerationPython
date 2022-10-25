# Трехзначное число
# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.

# На вход программе подаётся положительное трёхзначное число.

num = int(input())
# num = 154

unit = num % 10  # единицы
ten = (num // 10) % 10  # десятки
hundreds = num // 100  # сотни

"""
print(unit)
print(ten)
print(hundreds)
"""

sum = unit + ten + hundreds
print('Сумма цифр =', sum)
mul = unit * ten * hundreds
print('Произведение цифр =', mul)
