# Простые числа
"""
На вход программе подается два натуральных числа a и b (a< b).
 Напишите программу, которая находит все простые числа от a до b включительно.
"""

num1 = int(input())
num2 = int(input())
counter = 0
for i in range(num1, num2 + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
        if counter == 2:
            print(i)
