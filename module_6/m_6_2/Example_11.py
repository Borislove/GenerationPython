# Отдыхаем ли?
"""
Напишите программу, которая считывает одну строку, после чего выводит «YES»,
если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.
"""

"""
if 'суббота' in s or 'воскресенье' in s:
    print('YES')
else:
    print('NO')
"""
s = input()

s_test1 = 'суббота' in s
s_test2 = 'воскресенье' in s

if s_test1 or s_test2:
    print('YES')
else:
    print('NO')

# воскресенье  , воскресенье
