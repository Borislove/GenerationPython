# Наименьшее из четырёх чисел 🌶️

"""
#v1
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

less = 0

if num1 < num2:
    less = num1
else:
    less = num2

if less < num3:
    less = less
else:
    less = num3

if less < num4:
    less = less
else:
    less = num4

print(less)
"""

"""
# интересно
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)
"""

# print(min(int(input()), int(input()), int(input()), int(input())))

# v2
lst = [int(input()) for _ in range(4)]
print(min(lst))

# v2_1
print(min(int(input()) for _ in range(4)))
