# подсчитать количество чисел из диапазона [1;100], квадрат которых оканчивается на 4.
counter = 0
for i in range(1, 101):
    if i**2 % 10 == 4:
        counter = counter + 1
print(counter)