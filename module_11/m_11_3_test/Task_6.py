# Список строк
"""
На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает из указанных строк список и выводит его.

Формат входных данных
На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.
"""

num = int(input())
lst = []
for _ in range(num):
    s = input()
    lst.append(s)
print(lst)

# print([input() for _ in range(int(input()))])
