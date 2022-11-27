# Большое число
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

square_a = a ** b
square_c = c ** d
sum = square_a + square_c
print(sum)
"""
# v2
"""
list_num = [0, 0, 0, 0]
for i in range(list_num):
    list_num[i] = int(input())
ab = list_num[0] ** list_num[1]
cd = list_num[2] ** list_num[3]
print(ab + cd)
"""
# v3
list_num = [0, 0, 0, 0]
for i in range(4):
    list_num[i] = int(input())
print(list_num[0] ** list_num[1] + list_num[2] ** list_num[3])

"""
a, b, c, d = [int(input()) for _ in range(4)]
print(a ** b + c ** d)
"""
