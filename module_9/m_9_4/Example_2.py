# Метод startswith()
"""
Метод startswith(<suffix>, <start>, <end>) определяет начинается ли исходная строка s подстрокой <suffix>.
Если исходная строка начинается с подстроки <suffix>,метод возвращает значение True, а если нет, то  False
"""

s = 'foobar'
print(s.startswith('foo'))
print(s.startswith('baz'))