# Dog age
"""
На вход программе подается число n – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в человеческих годах.

Формат входных данных
На вход программе подаётся натуральное число – количество собачьих лет.
"""

num = int(input())

count = 0

if 1 <= num <= 2:
    count += 10.5
    num -= 1
    if (1 == num):
        count += 10.5
        num -= 1
    print(count)
else:
    num = (num - 2) * 4 + 21
    print(num)
# print(count)


"""
a = int(input())
if a <= 2:
    print(a * 10.5)
else:
    print(((a - 2) * 4) + 21)
"""