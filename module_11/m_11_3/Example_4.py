"""
Метод append() добавляет строку 'python' целиком к списку,
а метод extend() разбивает строку 'python' на  символы 'p', 'y', 't', 'h', 'o', 'n' и их добавляет в качестве элементов списка.
"""

words1 = ['iq option', 'stepik', 'beegeek']
words2 = ['iq option', 'stepik', 'beegeek']

words1.append('python')
words2.extend('python')

print(words1)
print(words2)
