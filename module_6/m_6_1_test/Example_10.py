# Интересное число

"""
Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре.
Напишите программу, которая определяет интересное число или нет. Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».

Формат входных данных
На вход программе подается целое трехзначное число.
"""

num = int(input())

# разбивка по разрядам
unit = num // 100
tens = num // 10 % 10
hundreds = num % 10
#
a, b, c = hundreds, tens, unit
# min and max
min_digit = min(a, b, c)
max_digit = max(a, b, c)
# средняя цифра
average_digit = a + b + c - min_digit - max_digit

if average_digit == max_digit - min_digit:
    print('Число интересное')
else:
    print('Число неинтересное')

# проверки
print('разряд единиц', unit)
print('разряд десятков', tens)
print('разряд сотен', hundreds)
print('минимальная цифра', min_digit)
print('максимальная цифра', max_digit)
print('средняя цифра', average_digit)

print(a + b)
print(b + c)
print(a + c)
print(average_digit == a + c)
