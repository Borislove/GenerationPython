# Суммы двух
"""
На вход программе подается натуральное число n≥2, а затем n целых чисел.
Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3, и т.д.)
"""

"""
num = int(input())

tmp_lst = []
for _ in range(num):
    numbers = int(input())
    tmp_lst.append(numbers)
print(tmp_lst)

lst = []
for i in range(len(tmp_lst)-1):
    lst.append(tmp_lst[i] + tmp_lst[i + 1])
print(lst)
"""

tmp_lst = []
for _ in range(int(input())):
    tmp_lst.append(int(input()))

lst = []
for i in range(len(tmp_lst) - 1):
    lst.append(tmp_lst[i] + tmp_lst[i + 1])
print(lst)
