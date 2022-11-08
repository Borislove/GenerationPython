# else в цикле
num = int(input())
n = num
while n != 0:
    last = n % 10
    if last == 7:
        print('Число', num, 'содержит цифру 7')
        break
    n //= 10
else:
    print('Число', num, 'не содержит цифру 7')
