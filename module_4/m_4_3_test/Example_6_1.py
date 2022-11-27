num1, num2 = int(input()), int(input())
operation = str(input())
lst = ['+', '-', '*', '/']

if operation == lst[0]:
    print(num1 + num2)
elif operation == lst[1]:
    print(num1 - num2)
elif operation == lst[2]:
    print(num1 * num2)
elif operation == lst[3]:
    if num2 == 0:
        print('На ноль делить нельзя!')
    else:
        print(num1 / num2)
else:
    print('Неверная операция')
