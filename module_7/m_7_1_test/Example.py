# Python is awesome
"""
Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.
"""

# v1.0
for _ in range(10):
    print('Python is awesome!')

# v2.0
print('Python is awesome!\n' * 10)

# v1.1
[print('Python is awesome!') for _ in range(10)]
