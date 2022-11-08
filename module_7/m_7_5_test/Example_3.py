# max и min
"""Дано натуральное число n, ,n≥10. Напишите программу, которая определяет его максимальную и минимальную цифры."""
import math

num = int(input())
num_max = num

s_max = 'Максимальная цифра равна'
s_min = 'Минимальная цифра равна'

minimum = 10
maximum = 0

# минимальная цифра
while num:
    digit = num % 10
    if digit < minimum:
        minimum = digit
    num //= 10
print(s_min, minimum)

# максимальная цифра
while num_max:
    digit = num_max % 10
    if digit > maximum:
        maximum = digit
    num_max //= 10
print(s_max, maximum)
