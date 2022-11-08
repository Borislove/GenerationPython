# 2 версия программы:
# 2:10 min
num = int(input())
flag = True

for i in range(2, num // 2 + 1):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')
