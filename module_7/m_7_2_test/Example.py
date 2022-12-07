# Последовательность чисел 1

"""
m <=n
Напишите программу, которая выводит все числа от m до n включительно
"""

# Формат входных данных На вход программе подаются два целых числа m и n, каждое на отдельной строке.

# 1 , 9
"""
m, n = int(input()), int(input())
for i in range(m, n + 1):
    print(i)
"""
#
"""
for i in range(int(input()), int(input()) + 1):
    print(i)
"""

#
#print(*range(int(input()), int(input()) + 1), sep='\n')

[print(i) for i in range(int(input()), int(input(+1)))]