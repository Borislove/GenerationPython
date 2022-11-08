# Ревью кода-2 🌶️🌶️
mx = 1
s = 1
for i in range(10):
    x = int(input())
    if x < 0:
        s = x
    if x > mx:
        mx = x
    print(s)
    print(mx)

else:
    print('NO')
