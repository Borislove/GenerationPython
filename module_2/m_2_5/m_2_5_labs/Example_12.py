# Перестановка цифр
"""
Дано трехзначное число abc в котором все цифры различны.
Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.

Формат входных данных
На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.

Формат выходных данных
Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке:
abc,acb,bac,bca,cab,cba
"""
"""
num = int(input())

a = num // 100
b = num // 10 % 10
c = num % 10

print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
"""

"""
num = int(input())
a = str(num // 100)
b = str(num // 10 % 10)
c = str(num % 10)

s1 = str(a + b + c)
s2 = str(a + c + b)
s3 = str(b + a + c)
print(s1, s1[::-1], sep='\n')
print(s2, s2[::-1], sep='\n')
print(s3, s3[::-1], sep='\n')
"""

""""
# v3
num = int(input())
a, b, c = str(num // 100), str((num // 10) % 10), str(num % 10)
s1, s2, s3 = str(a + b + c), str(a + c + b), str(b + a + c)
print(s1, s1[::-1], sep='\n')
print(s2, s2[::-1], sep='\n')
print(s3, s3[::-1], sep='\n')
"""

"""
# v3_1
num = int(input())
a, b, c = str(num // 100), str((num // 10) % 10), str(num % 10)
s1, s2, s3 = str(a + b + c), str(a + c + b), str(b + a + c)
print(s1, s2, sep='\n')
print(s3, s2[::-1], sep='\n')
print(s3[::-1], s1[::-1], sep='\n')
"""

# v3_2
num = int(input())
a, b, c = str(num // 100), str((num // 10) % 10), str(num % 10)
s1, s2, s3 = str(a + b + c), str(a + c + b), str(b + a + c)
print(s1, s2, s3, s2[::-1], s3[::-1], s1[::-1], sep='\n')

"""""
# v5
a, b, c = input()
print(a + b + c, a + c + b, b + a + c, b + c + a, c + a + b, c + b + a, sep='\n')
"""
