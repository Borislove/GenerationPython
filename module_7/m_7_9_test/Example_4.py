# Цифровой корень
"""
На вход программе подается натуральное число nn. Напишите программу,
 которая находит цифровой корень данного числа.
  Цифровой корень числа n получается следующим образом: если сложить все цифры этого числа,
  затем все цифры найденной суммы и повторить этот процесс, то в результате будет получено однозначное число (цифра),
  которое и называется цифровым корнем данного числа.
"""

"""
num = int(input())

total = 0
while num > 9:
    tmp = total
    while num != 0:
        tmp += num % 10
        num //= 10
    num = tmp
    total = tmp
print(total)
"""


num = int(input())
while num > 9:
    total = 0
    while num !=0:
        total += num % 10
        num //= 10
    num = total
print(num)

