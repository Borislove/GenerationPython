# Упорядоченные цифры 🌶️
"""
Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
"""

"""
num = int(input())

text = ''
counter = 0
while num != 0:
    digit = num % 10
    if digit < (num // 10) % 10:
        counter += 1
    num //= 10

    if counter > len(str(num)):
        text = 'YES'
    else:
        text = 'NO'
print(text)
"""

num = int(input())
tmp = num
counter = 1
while num != 0:
    last_digit = num % 10
    if last_digit <= (num // 10) % 10:
        counter += 1
    num //= 10

flag = counter == len(str(tmp))
print('YES' if flag else 'NO')


"""
n = int(input())
while n % 10 <= n // 10 % 10:
    n //= 10
print('YES' if n < 10 else 'NO')
"""