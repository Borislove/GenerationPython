# Метод endswith()
"""
Метод endswith(<suffix>, <start>, <end>) определяет оканчивается ли исходная строка s подстрокой <suffix>.
Метод возвращает значение True если исходная строка оканчивается на подстроку <suffix> и False в противном случае
"""

s = 'foobar'
print(s.endswith('bar'))
print(s.endswith('baz'))