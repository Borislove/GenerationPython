# Переставить min и max
"""
На вход программе подается строка текста, содержащая различные натуральные числа.
Из данной строки формируется список чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.
"""

s = input().split()
lst = []
for c in s:
    lst.append(int(c))
max_num = max(lst)
min_num = min(lst)
max_index = lst.index(max_num)
min_index = lst.index(min_num)

lst[max_index], lst[min_index] = lst[min_index], lst[max_index]
print(*lst)
