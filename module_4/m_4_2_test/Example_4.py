# Красивое число 🌶️

"""
Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17.
Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES»,
если число является красивым, или «NO» в противном случае.

Формат входных данных
На вход программе подаётся натуральное число.
"""

"""
num = int(input())

if (1000 <= num <= 9999) and (num % 7 == 0 or num % 17 == 0):
    print('YES')
else:
    print('NO')

print(1045 % 7)
print(1045 % 17)
"""

"""
# v2.1
num = int(input())
flag1 = num % 7 == 0
flag2 = num % 17 == 0
if (len(str(num)) == 4) and (flag1 or flag2):
    print('YES')
else:
    print('NO')
"""

"""
# v2.2
num = int(input())
flag1 = num % 7 == 0 
flag2 = num % 17 == 0
flag_len = len(str(num)) == 4
print('YES' if flag_len and (flag1 or flag2) else 'NO')
"""
# v2.3
num = int(input())
flag = num % 7 == 0 or num % 17 == 0
flag_len = len(str(num)) == 4
print('YES' if flag_len and flag else 'NO')
