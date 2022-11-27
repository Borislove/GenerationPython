# Две старушки

"""
num1, num2, num3 = float(input()), float(input()), float(input())

v = num2 + num3
s = num1 / v

print(s)
"""

# v2.0
lst = [float(input()) for _ in range(3)]
print(lst[0] / (lst[1] + lst[2]))

"""
s, v, v1 =[float(input()) for _ in range(3)]
print(s/(v+v1))
"""
