# 10 положительных чисел и находит среди них наибольшее число
largest = -1
for i in range(10):
    num = int(input())
    if num > largest:
        largest = num
print('Наибольшее число равно', largest)
