"""
Задача 1. Найдите все пары натуральных чисел (и их количество) являющихся решением уравнения 12x+13y = 12x+13y=777.
"""
total = 0
for x in range(1, 65):
    for y in range(1, 60):
        if 12 * x + 13 * y == 777:
            total += 1
            print('x =', x, 'y =', y)
print('Общее количество натуральных решений =', total)