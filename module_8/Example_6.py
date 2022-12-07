# Все вместе 2
"""
Дано натуральное число. Напишите программу, которая вычисляет:

количество цифр 3 в нем; +
сколько раз в нем встречается последняя цифра; +
количество четных цифр; +
сумму его цифр, больших пяти; +
произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
"""

num = int(input())

num_3 = 0
last_num = 0
count_even = 0
sum_num = 0
mul_num = 1
count_num_digit_0 = 0
count_num_digit_5 = 0
remainder = num % 10

while num > 0:
    last_digit = num % 10

    if last_digit == 3:
        num_3 += 1

    if num % 10 == remainder:
        last_num += 1

    if last_digit % 2 == 0:
        count_even += 1

    if last_digit > 5:
        sum_num += last_digit

    if last_digit > 7:
        mul_num *= last_digit

    if last_digit == 0:
        count_num_digit_0 += 1

    if last_digit == 5:
        count_num_digit_5 += 1

    num //= 10

print(num_3)
print(last_num)
print(count_even)
print(sum_num)
print(mul_num)
print(count_num_digit_0 + count_num_digit_5)
