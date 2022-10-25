# Оператор not
age = int(input('Сколько вам лет?: '))
if not (age < 12):  # 12 разрешен!
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

print(12 < 12)  # False
print(11 < 12)  # True
print(13 < 12)  # False
