from math import pi

# Площадь и длина

"""
Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R
"""

r = float(input())  # r - радиус
area = pi * (r ** 2)
length_circle = 2 * pi * r

print(area)
print(length_circle)
