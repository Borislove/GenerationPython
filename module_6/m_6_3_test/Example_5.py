# Квадратное уравнение 🌶️🌶️
"""
from math import sqrt

num1, num2, num3 = float(input()), float(input()), float(input())
a, b, c = num1, num2, num3

x = 0
discriminant = d = float((b ** 2) - 4 * a * c)

x1 = 0
x2 = 0

if d == 0:  # 1 корень
    x = -b / (2 * a)
    print(x)
elif d > 0:  # 2 корня
    x2 = (-b - sqrt(d)) / (2 * a)
    # print(x2)
    x1 = (-b + sqrt(d)) / (2 * a)
    # print(x1)
    if x1 > x2:
        print(x1)
    else:
        print(x2)
else:
    print('Нет корней')

abs(-0.0)
"""

"""
print(min(x1, x2))
print(max(x1, x2))
"""

from math import sqrt

a, b, c = [float(input()) for _ in range(3)]
d = float((b ** 2) - 4 * a * c)
x1, x2 = 0, 0
if d == 0:
    print(-b / (2 * a))
elif d > 0:
    x2 = (-b - sqrt(d)) / (2 * a)
    x1 = (-b + sqrt(d)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep='\n')
else:
    print('Нет корней')
