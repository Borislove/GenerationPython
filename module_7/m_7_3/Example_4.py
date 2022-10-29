# считывает 10 чисел и определяет сумму тех из них, которые больше 10.
total = 0
for i in range(10):
    num = int(input())
    if num > 10:
        total = total + num
print('Сумма чисел больших 10 равна', total)
