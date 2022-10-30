# Асимптотическое приближение
from math import log

num = int(input())

total = 0
for i in range(num+1):
    if i != 0:
        total += (1 / i)
print(float(total - log(num)))


#print(1 + 1 / 2 + 1 / 3 + 1 / 4 + 1 / 5 + 1 / 6 + 1 / 7 + 1 / 8 + 1 / 9 + 1 / 10 - log(10))
