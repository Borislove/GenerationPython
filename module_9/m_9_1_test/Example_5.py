# В столбик 1
"""
На вход программе подается одна строка. Напишите программу, которая выводит элементы строки с индексами 0, 2, 4, ... в столбик.
"""

s = input()
for c in range(0, len(s), 2):
    print(s[c])
    print()
