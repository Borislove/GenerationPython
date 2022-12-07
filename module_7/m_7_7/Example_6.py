# Ревью кода-2 🌶️🌶️
mx = -10 ** 6 - 1
s = 0
for i in range(10):
    num = int(input())
    if num < 0:
        s += num
    if 0 > num > mx:
        mx = num
if s < 0:
    print(s)
    print(mx)
else:
    print('NO')
