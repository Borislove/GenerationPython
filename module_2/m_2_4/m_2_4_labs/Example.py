# Три последовательных числа
"""
Напишите программу вывода на экран трех последовательно идущих чисел,
 каждое на отдельной строке. Первое число вводит пользователь, остальные числа вычисляются в программе.
"""

"""
num_input = int(input())

num = num_input
print(num)
num += 1
print(num)
num += 1
print(num)
"""

"""
# v2
num = int(input())
for _ in range(3):
    print(num)
    num += 1
"""

# v3.0
print(sum(int(input()) for _ in range(3)))
