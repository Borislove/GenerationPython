# Делители 2
"""
Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.
"""


def get_factors(num):
    global counter
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    return counter


# объявление функции
def number_of_factors(num):
    return get_factors(num)


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
