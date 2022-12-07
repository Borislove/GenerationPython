# Вторая цифра
"""Дано натуральное число n, n>9. Напишите программу, которая определяет его вторую (с начала) цифру."""

num = int(input())
tmp = 0

while num != 0:
    last_digit = num % 10
    if num >= 10:
        tmp = last_digit
    num //= 10

print(tmp)

# print(input()[1])
