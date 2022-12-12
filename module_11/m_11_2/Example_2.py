# Оператор принадлежности in
"""
Оператор in позволяет проверить, содержит ли список некоторый элемент.
"""

numbers = [2, 4, 6, 8, 10]

if 2 in numbers:
    print('Список numbers содержит число 2')
else:
    print('Список numbers не содержит число 2')

"""
можем использовать оператор in вместе с логическим оператором not. Например
"""
numbers1 = [2, 4, 6, 8, 10]

if 0 not in numbers1:
    print('Список numbers не содержит нулей')