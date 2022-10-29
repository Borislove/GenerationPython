from math import pi, tan

# Правильный многоугольник

n, a = float(input()), float(input())
square = (n * a ** 2) / (4 * tan( (pi / n)))
print(square)
