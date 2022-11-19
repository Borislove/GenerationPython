# ОБЪЕМ КУБА
# Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому значению длины ребра.

"""
length = int(input())
volume = length * length * length
print('Объем =', volume)

square = 6 * (length * length)
print('Площадь полной поверхности =', square)
"""
# v2
length = int(input())

volume = length ** 3
print('Объем =', volume)

square = 6 * (length ** 2)
print('Площадь полной поверхности =', square)
