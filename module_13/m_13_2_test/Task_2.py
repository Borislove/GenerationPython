# Звездный треугольник
"""
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.
"""


# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base + 1):
        print(fill * min(i, base - i + 1))


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
