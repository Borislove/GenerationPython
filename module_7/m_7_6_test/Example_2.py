# Наименьший делитель
"""
На вход программе подается число n>1. Напишите программу, которая выводит его наименьший отличный от 1 делитель.
"""

num = int(input())

tmp = 0
for i in range(2, num): 
    if num % i == 0:
        tmp = i
        break
    if (num // num == 1):
        tmp = num
        continue
print(tmp)

"""
n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break     
"""