# Цвет настроения синий
"""
Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.

Формат входных данных
На вход программе подается одна строка.
"""

s = input()

if 'синий' in s:
    print('YES')
else:
    print('NO')

# print('YES' if 'синий' in input() else 'NO')