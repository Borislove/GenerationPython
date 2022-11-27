# Размножение n-ок

num = int(input())
"""
num_1 = num
num_2 = num * 10
num_3 = num * 100

sum = num_1 * 3 + num_2 * 2 + num_3
print(sum)
"""
# v2
total = 0
for i in range(3):
    total += i
    i *= 10
print(total)

"""
print(int(input()) * 123)
"""
