# Евклидово расстояние


x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

from math import sqrt

p = sqrt((x1-x2)**2 + (y1-y2)**2)
print(p)