# Последовательность чисел 4

"""
число кратно 17;
число оканчивается на 9;
число кратно 3 и 5 одновременно.
"""

# На вход программе подаются два натуральных числа m и n  (m<=n)

"""
число кратно 17;
число оканчивается на 9;
число кратно 3 и 5 одновременно.
"""

num1, num2 = int(input()), int(input())
m = num1
n = num2

for i in range(m, n+1):
    if i % 17 == 0:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print(i)
    elif i%10 == 9:
        print(i)

# elif (m % 3 == 0) and (m % 5 == 0):
#           print(m)
