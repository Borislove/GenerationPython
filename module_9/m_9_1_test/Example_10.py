# Сколько раз?

"""
На вход программе подается одна строка. Напишите программу, которая определяет сколько раз в строке встречаются символы + и *.
"""

s = input()

counter1 = 0
counter2 = 0
for i in range(len(s)):
    if s[i] in ['+']:
        counter1 += 1
    elif s[i] in ['*']:
        counter2 += 1
print('Символ + встречается', counter1, 'раз')
print('Символ * встречается', counter2, 'раз')


"""
n = input()
print("Символ + встречается", n.count("+"), "раз")
print("Символ * встречается", n.count("*"), "раз")
"""