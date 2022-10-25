# Значение функции
# Напишите программу вычисления значения функции f(a,b) = 3(a + b)^3 + 275b^2 - 127a - 41

a = int(input())
b = int(input())

num1 = 3 * ((a + b) * (a + b) * (a + b))
num2 = 275 * b * b
num3 = 127 * a

decision = num1 + num2 - num3 - 41
print(decision)
