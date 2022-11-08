# Гипотеза Эйлера о сумме степеней 🌶️🌶️

from math import sqrt

num = 150
counter = 0
total = 0

"""
from timeit import default_timer as timer

start_time = timer()

for a in range(1, num):
    for b in range(1, num):
        for c in range(1, num):
            for d in range(1, num):
                for e in range(1, num):
                    counter += 1
                    if (a ** 5 + b ** 5 + c ** 5 + d ** 5) == (e ** 5):
                        total += 1
                        print(a + b + c + d + e)
                    print('a = ', a, 'b = ', b, 'c = ', 'd =', d, 'e =', e)
                print('counter', counter)
print('total', total)

print()
print("Время выполнения: {:g} сек".format(timer() - start_time))

"""

total = 0
for a in range(1, 150):
    for b in range(a, 150):
        for c in range(b, 150):
            for d in range(c, 150):
                e = (a ** 5 + b ** 5 + c ** 5 + d ** 5) ** 0.2
                if (int(e)) == round(e, 10):
                    total += 1
                    print('a = ', a, 'b = ', b, 'c = ', 'd =', d, 'e =', e)
print('Общее количество натуральных решений = ', total)
