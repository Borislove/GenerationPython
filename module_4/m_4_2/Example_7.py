a = int(input())  # 7
if a >= 2 and a <= 17:  # 7 and 7
    b = 3
    p = a * a + b * b
else:
    b = 5
p = (a + b) * (a + b)  # после else - подсчет отсюда
print(p)
