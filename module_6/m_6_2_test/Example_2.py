# What's Your Name?

"""
Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:

«Hello [введенное имя] [введенная фамилия]! You just delved into Python».
"""

first_name, last_name = input(), input()

s1 = 'Hello '
s2 = ' You just delved into Python '

print(s1 + first_name, last_name + '!' + s2)
