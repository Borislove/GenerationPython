# Последовательность символов
# Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:

"""
#   v1.0
for i in range(6):
    print('A' * 3)
print('E')
for i in range(5):
    print('B' * 4)
for i in range(9):
    print('T' * 9)
print('G')
"""

"""
# v1.1
[print('A' * 3) for _ in range(6)]
[print('B' * 4) for _ in range(5)]
print('E')
[print('T' * 5) for _ in range(9)]
print('G')
"""

"""
# v2.0 
def printer(i, ch, x):  # i - count repeat, ch - symbol, x - count ch
    [print(ch * x) for _ in range(i)]


printer(6, 'A', 3)
printer(5, 'B', 4)
print('E')
printer(9, 'T', 5)
print('G')
"""

# print('AAA\n'*6 + 'BBBB\n'*5 + 'E\n' + 'TTTTT\n'*9 + 'G')
