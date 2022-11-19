# Значение функции

"""
# v1
a, b = int(input()), int(input())


def double(num):
    return num ** 2


def cube(num):
    return num ** 3


def sum():
    return a + b

# f(a,b) = 3(a + b)^3 + 275b^2 - 127a - 41
print(3 * (cube(sum())) + 275 * double(b) - 127 * a - 41)
"""

"""
# v2
a, b = int(input()), int(input())


def function(a, b):
    return 3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41


print(function(a, b))
"""

a = int(input())
b = int(input())
print(3 * (a + b) ** 3 + 275 * (b ** 2) - 127 * a - 41)
