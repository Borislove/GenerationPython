# Заглавные буквы
"""
На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним пробелом.
Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
"""

"""
s = input()
if s.title() in s:
    print('YES')
else:
    print('NO')
"""

s = input()
print('YES' if s.title() in s else 'NO')

print('YES' if input().istitle() else 'NO')

print(['NO', 'YES'][input().istitle()])