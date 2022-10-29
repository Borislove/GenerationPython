# Тригонометрическое выражение
from math import sin, cos, tan, radians

x = float(input())
x_radians = radians(x)
x = x_radians

formula = sin(x) + cos(x) + ((tan(x)) ** 2)

print(formula)
