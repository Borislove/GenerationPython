# Пока делимся

"""
На вход программе подается последовательность целых чисел делящихся на 7,
каждое число на отдельной строке. Концом последовательности является любое число не делящееся на 7.
 Напишите программу, которая выводит члены данной последовательности.

Формат входных данных
На вход программе подается последовательность чисел, каждое число на отдельной строке.
"""

flag = True
while flag:
    num = int(input())
    if (num % 7) == 0:
        print(num)
    else:
        flag = False

