num = int(input())
max_digit = 0
while num != 0:
    digit = num % 10
    if digit % 3 == 0:
        max_digit = digit
    num //= 10
if max_digit == 0:
    print('NO')
else:
    print(max_digit)


