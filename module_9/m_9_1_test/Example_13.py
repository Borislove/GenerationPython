# Decimal to Binary
"""
На вход программе подается натуральное число,
записанное в десятичной системе счисления. Напишите программу, которая переводит данное число в двоичную систему счисления.
"""

num = int(input())

lst = []
while num != 0:
    remainder = num - num % 2
    lst.append(num - remainder)
    num //= 2

lst.reverse()
print(*lst, sep='')


"""
n = int(input())
total = ''
while n > 0:
    if n % 2 == 0:
        total += '0'
    else:
        total += '1'
    n //= 2
total = total[::-1]
print(total)
"""