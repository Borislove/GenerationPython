# Алфавит
"""
Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
"""

lst = []
for i in range(26):
    lst.append(chr(ord('a') + i) * (i + 1))
print(lst)
