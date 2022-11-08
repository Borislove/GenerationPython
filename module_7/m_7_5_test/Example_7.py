# Упорядоченные цифры 🌶️
"""
Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
"""

num = int(input())

text = ''
counter = 0
while num != 0:
    digit = num % 10
    if digit < (num // 10) % 10:
        counter += 1
    num //= 10

    if (counter > len(str(num))):
        text = 'YES'
    else:
        text = 'NO'
print(text)
