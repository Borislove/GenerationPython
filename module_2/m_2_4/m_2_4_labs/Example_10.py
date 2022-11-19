# Разделяй и властвуй

# 7---14---21---28---35

"""
num = int(input())

x = num
x2 = x * 2
x3 = x * 3
x4 = x * 4
x5 = x * 5

print(x, x2, x3, x4, x5, sep='---')
"""

# v2
num = int(input())
for i in range(1, 6):
    if i == 5:
        print(num * i)
        break
    print(num * i, end='---')
