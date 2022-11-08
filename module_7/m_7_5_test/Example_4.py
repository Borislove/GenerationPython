# Все вместе

"""
Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
"""

# На вход программе подается одно натуральное число

num = int(input())
tmp_num = num
s = str(num)
s_len = len(s)

sum = 0
mul = 1
average = 0
first_digit = 0
last_digit = 0
flag = True
counter = -1
a = 10

# последняя цифра
last_digit_tmp = num % 10

while flag:
    # сумма всех цифр
    last_digit = num % 10
    sum += last_digit
    mul *= last_digit
    num //= 10
    counter += 1
    if num == 0:
        flag = False

average = sum / s_len
print(sum)
print(s_len)
print(mul)
print(average)
a = a ** counter
tmp_num = tmp_num // a
print(tmp_num)
print(tmp_num + last_digit_tmp)
