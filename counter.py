# подсчет одинаковых цифр
num = 612346665660156
remainder = num % 10
cnt = 0
while num != 0:
    if num % 10 == remainder:
        cnt += 1
    num //= 10
print(cnt)
