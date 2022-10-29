# Сумма чисел

"""
На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел.
"""

num1 = int(input())

total = 0
for i in range(num1):
    num2 = int(input())
    total += num2
# print('temp_total', total)
print(total)

