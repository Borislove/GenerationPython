# Трехзначное число
# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.

# На вход программе подаётся положительное трёхзначное число.


"""
num = int(input())

unit = num % 10  # единицы
ten = (num // 10) % 10  # десятки
hundreds = num // 100  # сотни

sum = unit + ten + hundreds
print('Сумма цифр =', sum)
mul = unit * ten * hundreds
print('Произведение цифр =', mul)
"""

"""
# v2

num = int(input())

mul = 1
add = 0
for _ in range(1, len(str(num)) + 1):
    remains = num % 10
    mul *= remains
    add += remains
    num //= 10
print('Сумма цифр =', add)
print('Произведение цифр =', mul)
"""


n = 777
sum = 0
q = 1
for i in str(n):
    sum += int(i)
    q *= int(i)
print(f'Сумма цифр = {sum}')
print(f'Произведение цифр = {q}')
