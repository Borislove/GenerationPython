# Метод copy()
"""
Метод copy() создает поверхностную копию списка.
"""

"""
# 1
names = ['Gvido', 'Roman', 'Timur']
names_copy = names.copy()  # создаем поверхностную копию списка names

print(names)
print(names_copy)
"""

# 2
names = ['Gvido', 'Roman', 'Timur']
names_copy1 = list(names)  # создаем поверхностную копию с помощью функции list()
names_copy2 = names[:]  # создаем поверхностную копию с помощью среза от начала до конца
