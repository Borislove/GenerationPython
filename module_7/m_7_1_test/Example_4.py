# Квадрат числа

"""
На вход программе подается натуральное число n. Напишите программу,
которая для каждого из чисел от 0 до n (включительно) выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).
"""

num = int(input())

for num in range(num + 1):
    print('Квадрат числа', num, 'равен', num * num)
    # print('Квадрат числа', num, 'равен', num **2)
