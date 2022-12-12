# Значение функции
"""
На вход программе подается натуральное число n, а затем n целых чисел.
Напишите программу, которая для каждого введенного числа x выводит значение функции f(x) = x^2 + 2x + 1
, каждое на отдельной строке.
"""

num = int(input())

lst = []
tmp_lst = []
for i in range(num):
    x = int(input())
    tmp_lst.append(x)
    lst.append(x ** 2 + 2 * x + 1)
print(*tmp_lst, sep='\n')
print()
print(*lst, sep='\n')
