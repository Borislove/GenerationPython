# Следуй правилам
"""
На вход программе подается натуральное число n. Напишите программу, которая выводит числа от 1 до n включительно за исключением:

чисел от 5 до 9 включительно;
чисел от 17 до 37 включительно;
чисел от 78 до 87 включительно.
"""

num = int(input())

for i in range(1,num+1):
    if 5 <= i <= 9:
        continue
    elif 17 <= i <= 37:
        continue
    elif 78 <= i <= 87:
        continue
    print(i)