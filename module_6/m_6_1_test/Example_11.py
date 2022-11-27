# Абсолютная сумма

"""
a1, a2, a3, a4, a5 = abs(float(input())), abs(float(input())), abs(float(input())), abs(float(input())), abs(
    float(input()))

add = a1 + a2 + a3 + a4 + a5
print(add)
"""

# v2.1
lst = [float(input()) for _ in range(5)]

total = 0
for i in range(len(lst)):
    total += abs(lst[i])
print(total)

# v2.3
print(sum([abs(float(input())) for _ in range(5)]))
