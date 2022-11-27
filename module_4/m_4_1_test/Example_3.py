# Соотношение
"""
Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
сумма первой и последней цифр равна разности второй и третьей цифр.
"""

"""
num = int(input())

unit = num % 10  # единицы
ten = (num // 10) % 10  # десятки
hundreds = num // 100 % 10  # сотни
thousand = num // 1000  # тысячи

if thousand + unit == hundreds - ten:
    print('ДА')
else:
    print('НЕТ')
"""

"""
# v2
a, b, c, d = input()
if int(a) + int(d) == int(b) - int(c):
    print('ДА')
else:
    print('НЕТ')
"""

# v3
a, b, c, d = input()
lst = [a, b, c, d]


def converter(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst


converter(lst)
if lst[0] + lst[3] == lst[1] - lst[2]:
    print('ДА')
else:
    print('НЕТ')

# v4
