# YES or NO вот в чем вопрос
"""
Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».

Условия:

если число нечётное, то вывести «YES»;
если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
если число чётное и больше 20, то вывести «NO».
Формат входных данных
На вход программе подаётся натуральное число.
"""

num = int(input())

even_integer = (num % 2 == 0)  # четное число

if (20 < num) and even_integer:
    print('NO')
elif (2 <= num <= 5) and even_integer:
    print('NO')
elif (6 <= num <= 20) and even_integer:
    print('YES')
else:
    print('YES')
