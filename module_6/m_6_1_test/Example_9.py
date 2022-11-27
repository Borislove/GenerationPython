# Сортировка трёх 🌶️

"""
Напишите программу, которая упорядочивает три числа от большего к меньшему.

Формат входных данных
На вход программе подается три целых числа, каждое на отдельной строке.
"""

"""
num1, num2, num3 = int(input()), int(input()), int(input())

min_number = min(num1, num2, num3)
max_number = max(num1, num2, num3)

average = num1 + num2 + num3 - min_number - max_number
print(max_number, average, min_number , sep='\n')
"""

# v2.0
print(*sorted(int(input()) for _ in range(3))[::-1], sep='\n')

# print(*sorted([int(input()) for _ in range(3)], reverse=True), sep='\n')
