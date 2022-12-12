# Метод isalnum()
"""
Метод isalnum() определяет, состоит ли исходная строка из буквенно-цифровых символов.
Метод возвращает значение True если исходная строка является непустой и состоит только из буквенно-цифровых символов и False в противном случае.
"""

s1 = 'abc123'
s2 = 'abc$*123'
s3 = ''

print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())