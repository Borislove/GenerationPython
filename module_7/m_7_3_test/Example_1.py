# Сумма чисел

"""
На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел.
"""

"""
num1 = int(input())

total = 0
for i in range(num1):
    num2 = int(input())
    total += num2
# print('temp_total', total)
print(total)
"""

"""
#v1.1
num1 = int(input())

total = 0
for _ in range(num1):
    total += int(input())
print(total)
"""

# v1.2
total = 0
for _ in range(int(input())):
    total += int(input())
print(total)
