# Количество цифр
"""
На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.
"""

s = input()
counter = 0
for i in range(len(s)):
    if s[i].isdigit():
        counter += 1
print(counter)

"""
count = 0
for c in input():
    if c.isdigit():
        count += 1
print(count)
"""

"""
s = input()
sum = 0
for i in range (len(s)):
    if s[i] in "0123456789":
        sum += 1
print (sum)
"""
