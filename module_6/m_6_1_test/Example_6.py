# Первая цифра после точки
# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

num = float(input())
integer = int(num)
total = num - integer
total *= 10

print('total', int(total))

print(int((num % 1)*10))

# XD
print(float(input(int((num%1)*10))))