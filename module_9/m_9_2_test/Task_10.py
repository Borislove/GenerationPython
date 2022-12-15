# Две половинки
"""
На вход программе подается строка текста. Напишите программу, которая разрежет ее на две равные части, переставит их местами и выведет на экран.
"""

s = input()
lst = []
if len(s) % 2 != 0:
    s += ''
    slice = len(s) // 2 + len(s) % 2
    lst.append(s[slice:].strip())
    lst.append(s[:slice])
    print(*lst, sep='')
else:
    slice = len(s) // 2 + len(s) % 2
    lst.append(s[slice:])
    lst.append(s[:slice])
    print(*lst, sep='')

"""
from math import *
s = input()
i = ceil(len(s)/2)
print(s[i:]+s[:i])
"""
