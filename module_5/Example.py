# Начало столетия

"""
Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля.
Если год оканчивается, то выведите «YES», иначе выведите «NO».

Формат входных данных
На вход программе подаётся натуральное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
"""
"""
num = int(input())

units = num % 10 == 0  # единицы
dozens = num % 100 == 0  # десятки
check = units and dozens

if check:
    print('YES')
else:
    print('NO')
"""

"""test
print(num)
print(num % 10, units)
print(num % 100, dozens)

# -------------------------
x = int(input())
if x % 100 == 0:
    print('YES')
else:
    print('NO')
"""

"""
num = int(input())
count = 0
for _ in range(2):
    if num % 10 == 0:
        count += 1
    num //= 10
print('YES' if count == 2 else 'NO')
"""

print('YES' if int(input()) % 100 == 0 else 'NO')

# print('YES' if input()[-2:] == '00' else 'NO')