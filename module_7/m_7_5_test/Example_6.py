# Одинаковые цифры
"""
Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
"""

"""
num = int(input())
s = ''

if num == len(str(num)):
    print('YES')

while len(str(num)) != 1:
    if (num % 10 == (num // 10) % 10):
        s = 'YES'
    else:
        s = 'NO'
        num = 1
    num //= 10
print(s)
"""


num = int(input())
while num % 10 == num // 10 % 10:
    num //= 10
print('YES' if num < 10 else 'NO')