# Римские цифры

"""
Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру.
Если число находится вне диапазона 1-10, то программа должна вывести текст «ошибка».

В таблице приведены римские цифры для чисел от 1 до 10.
"""

"""
num = int(input())

if num == 1:
    print('I')
elif num == 2:
    print('II')
elif num == 3:
    print('III')
elif num == 4:
    print('IV')
elif num == 5:
    print('V')
elif num == 6:
    print('VI')
elif num == 7:
    print('VII')
elif num == 8:
    print('VIII')
elif num == 9:
    print('IX')
elif num == 10:
    print('X')
else:
    print('ошибка')
    
"""
# v2.0
num = int(input())
lst = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
for i in range(len(lst)):
    if i == num:
        print(lst[i])
        break
else:
    print('ошибка')