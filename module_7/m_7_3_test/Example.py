# Количество чисел

"""
На вход программе подаются два целых числа a и b a≤b.
Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно, куб которых оканчивается на 4 или 9.
"""

# Примечание. Куб числа a – это его третья степень a^3

num1, num2 = int(input()), int(input())
a, b = num1, num2

counter = 0
if a <= b:
    for i in range(a, b + 1):
        if (i ** 3 % 10) == 4:
            counter += 1
            #print(counter)
        if (i ** 3 % 10) == 9:
            counter +=1
            #print(counter)
    print(counter)


