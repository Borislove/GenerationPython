# Список букв
"""
На вход программе подается одно число n.
Напишите программу, которая выводит список, состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.
"""

num = int(input())

lst = []
for i in range(97, 97 + num):
    lst.extend(chr(i))
print(lst)