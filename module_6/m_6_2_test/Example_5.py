# Арифметические строки
""" Вводятся 3 строки в случайном порядке. Напишите программу,
которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
"""

# (2b-c-a)(2c-b-a)(2a-b-c) = 0

"""
s1, s2, s3 = input(), input(), input()

s1_length = len(s1)
s2_length = len(s2)
s3_length = len(s3)

a, b, c = s1_length, s2_length, s3_length

if (2 * b - c - a) * (2 * c - b - a) * (2 * a - b - c) == 0:
    print('YES')
else:
    print('NO')
"""

# v2.0
"""
lst = [input() for _ in range(3)]
print('YES' if ((2 * len(lst[1]) - len(lst[2]) - len(lst[0]))
                * (2 * len(lst[2]) - len(lst[1]) - len(lst[0]))
                * (2 * len(lst[0]) - len(lst[1]) - len(lst[2])) == 0) else 'NO')

# v2.1
"""
lst = [0, 0, 0]
for i in range(len(lst)):
    lst[i] = len(input())
print('YES' if ((2 * lst[1] - lst[2] - lst[0])
                * (2 * lst[2] - lst[1] - lst[0])
                * (2 * lst[0] - lst[1] - lst[2]) == 0) else 'NO')

# v3.1
# a, b, c = len(input()), len(input()), len(input())
a, b, c = [len(input()) for _ in range(3)]
# print('YES' if (2 * a - b - c) * (2 * b - c - a) * (2 * c - a - b) == 0 else 'NO')
print('YES' if (-a - b + 2.0 * c) * (-a - c + 2.0 * b) * (-b - c + 2.0 * a) == 0 else 'NO')
