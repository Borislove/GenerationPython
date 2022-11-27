# Арифметическая прогрессия

"""
num1 = int(input())
num2 = int(input())
num3 = int(input())

total = (num2 - num1) + num2 == num3

if total:
    print('YES')
else:
    print('NO')
"""

# v2
lst = [int(input()) for _ in range(3)]
if lst[2] - lst[1] + lst[2] == lst[3]:
    print('YES')
else:
    print('NO')

# v2_1
lst = [int(input()) for _ in range(3)]
flag = (lst[1] - lst[0] + lst[1] == lst[2])
print('YES' if flag else 'NO')

# print('YES' if sum([int(input()) for _ in range(3)]) % 3 == 0 else 'NO')
