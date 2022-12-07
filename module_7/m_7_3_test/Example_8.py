# Only even numbers 🌶️

"""
Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.
"""

"""
counter = 0
for i in range(10):
    num = int(input())
    if (num % 2 == 0):
        counter += 1

if counter == 10:
    print('YES')
else:
    print('NO')
"""

"""
# v1.1
counter = 0
for _ in range(10):
    num = int(input())
    if num % 2 == 0:
        counter += 1
print('YES' if counter == 10 else 'NO')
"""
# v1.2
counter = 0
for _ in range(10):
    if int(input()) % 2 == 0:
        counter += 1
print('YES' if counter == 10 else 'NO')

"""
flag = 'YES'
for _ in range(10):
    a = int(input())
    if a % 2 != 0:
        flag = 'NO'
print(flag)
"""

"""
flag = 'YES'
for _ in range(10):
    if int(input()) % 2 != 0:
        flag = 'NO'
print(flag)
"""

flag = True
for _ in range(10):
    if int(input()) % 2 != 0:
        flag = False
print("YES" if flag else "NO")
