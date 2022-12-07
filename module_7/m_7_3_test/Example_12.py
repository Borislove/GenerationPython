# Наибольшие числа 🌶️🌶️

"""
На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
"""

"""
tmp_1 = 0
tmp_2 = 0
for _ in range(int(input())):  # ввод кол-во чисел
    num = int(input())
    if num > tmp_1:
        tmp_2 = tmp_1
        tmp_1 = num
    elif num > tmp_2:
        tmp_2 = num

print(tmp_1)
print(tmp_2)
"""

max1, max2 = 0, 0
for _ in range(int(input())):  # ввод кол-во чисел
    num = int(input())
    if num > max1:
        max2, max1 = max1, num
    elif num > max2:
        max2 = num
print(max1, max2, sep='\n')
