# Метод count()
"""
Метод count(<sub>, <start>, <end>) считает количество непересекающихся вхождений подстроки <sub> в исходную строку s
"""

s = 'foo goo moo'
print(s.count('oo'))
print(s.count('oo', 0, 8))  # подсчет с 0 по 7 символ