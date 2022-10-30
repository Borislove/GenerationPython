# Знакочередующаяся сумма

num = int(input())

total = 0
for i in range(num + 1):
    total += (-1) ** (i + 1) * i
print(total)
