# Средние значения

"""
num1, num2 = float(input()), float(input())
a, b = num1, num2


arithmetic = (a + b) / 2
# среднее геометрическое чисел
geometric = (a * b) ** 0.5
# среднее гармоническое чисел
harmonic = (2 * a * b) / (a + b)
# среднее квадратичное чисел
quadratic = ((a ** 2 + b ** 2) / 2) ** 0.5

print(arithmetic)
print(geometric)
print(harmonic)
print(quadratic)

"""
# v1.1
a = float(input())  # number a
b = float(input())  # number b

arithmetic = (a + b) / 2  # среднее арифметическое чисел

geometric = (a * b) ** 0.5  # среднее геометрическое чисел

harmonic = (2 * a * b) / (a + b)  # среднее гармоническое чисел

quadratic = ((a ** 2 + b ** 2) / 2) ** 0.5  # среднее квадратичное чисел

print(arithmetic, geometric, harmonic, quadratic, sep='\n')
