# Задача 2. Напишите программу, которая определяет,
# состоит ли двузначное число, введенное с клавиатуры,
# из одинаковых цифр. Если состоит, то программа выводит «ДА», в противном случае программа выводит «НЕТ».

num = int(input())
last_digit = num % 10    # последняя цифра числа
first_digit = num // 10  # первая цифра числа

if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')