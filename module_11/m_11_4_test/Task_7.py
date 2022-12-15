# Negatives, Zeros and Positives
"""
На вход программе подается натуральное число n, а затем n целых чисел.
Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа,
каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.
"""

num = int(input())

negative_num = []
zero = []
positive_num = []
for i in range(num):
    numbers = int(input())
    if numbers < 0:
        negative_num.append(numbers)
    elif numbers == 0:
        zero.append(numbers)
    else:
        positive_num.append(numbers)

lst = negative_num + zero + positive_num
print(*lst, sep='\n')
