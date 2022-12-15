# Самый частотный символ
"""
На вход программе подается строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
"""

s = input().lower()
counter = 0
char = ''
for i in range(len(s)):
    s2 = s.count(s[i])
    if s2 >= counter:
        counter = s2
        char = s[i]
print(char)