# Принадлежность 3

#  -30....-2_____7....25   ---> x


"""
num = int(input())
if (num > -30 and num <= -2) or (num > 7 and num <= 25):
    print('Принадлежит')
else:
    print('Не принадлежит')
"""

"""
# v1.2
num = int(input())
if -2 >= num >= -30 or 7 < num <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')
"""

# v2
num = int(input())
flag1 = -2 >= num > -30
flag2 = 7 < num <= 25
print('Принадлежит' if flag1 or flag2 else 'Не принадлежит')
