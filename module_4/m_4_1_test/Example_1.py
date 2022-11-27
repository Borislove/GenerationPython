# Пароль
"""
Напишите программу, которая сравнивает пароль и его подтверждение.
Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».
"""

"""
str1 = input()  # пароль
str2 = input()  # подтверждение пароля

if str1 == str2:
    print('Пароль принят')
else:
    print('Пароль не принят')
"""

"""
if input() == input():
    print('Пароль принят')
else:
    print('Пароль не принят')
"""

# v1_2
input_password, check_password = input(), input()
if input_password == check_password:
    print('Пароль принят')
else:
    print('Пароль не принят')


"""
print("Пароль принят" if input() == input() else "Пароль не принят")
"""
