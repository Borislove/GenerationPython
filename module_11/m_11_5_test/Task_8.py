# Количество совпадающих пар
"""
На вход программе подается строка текста, содержащая натуральные числа.
Из данной строки формируется список чисел. Напишите программу, которая подсчитывает,
сколько в полученном списке пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""

# 1 7 5 7 5
s = input().split()
counter = 0
for i in range(len(s)):
    for q in range(i + 1, len(s)):
        if s[i] == s[q]:
            counter += 1
print(counter)
