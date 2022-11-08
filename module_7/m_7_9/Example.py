# Численный треугольник 3

n = int(input())*2-1
m = 1

for i in range(1,n+1):
    s = min(i, n-i+1)
    for k in range(s):
        print(m, end=' ')
        m += 1
    print()