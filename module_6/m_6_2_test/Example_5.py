# Арифметические строки
""" Вводятся 3 строки в случайном порядке. Напишите программу,
которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
"""

# (2b-c-a)(2c-b-a)(2a-b-c) = 0
s1, s2, s3 = input(), input(), input()

s1_length = len(s1)
s2_length = len(s2)
s3_length = len(s3)

a, b, c = s1_length, s2_length, s3_length

if (2 * b - c - a) * (2 * c - b - a) * (2 * a - b - c) == 0:
    print('YES')
else:
    print('NO')