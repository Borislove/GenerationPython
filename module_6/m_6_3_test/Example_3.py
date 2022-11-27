# Тригонометрическое выражение
from math import sin, cos, tan, radians, pow

"""
x = float(input())
x_radians = radians(x)
x = x_radians

formula = sin(x) + cos(x) + ((tan(x)) ** 2)

print(formula)

"""
x = radians(float(input()))
print(sin(x) + cos(x) + pow(tan(x), 2))
