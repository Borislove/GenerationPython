# Цифра 1
"""
На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.
"""

s = input()
total = 0
for i in range(len(s)):
    total += int(s[i])
print(total)


# print(sum(int(i) for i in input()))