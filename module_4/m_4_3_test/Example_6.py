# Самописный калькулятор 🌶️

"""
Напишите программу, которая считывает с клавиатуры два целых числа и строку.
Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /),
то выведите результат применения этой операции к введённым ранее числам, в противном случае выведите «Неверная операция».
Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».

Формат входных данных
На вход программе подаются два целых числа, каждое на отдельной строке, и строка.

Формат выходных данных
Программа должна вывести результат применения операции к введенным числам или соответствующий текст,
если операция неверная либо если происходит деление на ноль.
"""
# calc

num1, num2 = int(input()), int(input())
operation = str(input())

# default
add = 0  # сложение  --sum зарезервировано--
sub = 0  # вычитание
mul = 0  # умножение
div = 0  # деление

# calculations
if operation == '+' or operation == '-' or operation == '*' or operation == '/':
    if operation == '+':
        add = num1 + num2
        print(add)
    elif operation == '-':
        sub = num1 - num2
        print(sub)
    elif operation == '*':
        mul = num1 * num2
        print(mul)
    elif operation == '/':
        if num2 == 0:
            print('На ноль делить нельзя!')
        else:
            div = num1 / num2
            print(div)
else:
    print('Неверная операция')

# result calc
if operation == '+':
    print(sum)
elif operation == '-':
    print(sub)
elif operation == '*':
    print(mul)
elif (operation == '/') and num2 != 0:
    print(div)

# result который не работает
"""
match operation:
    case "+":
        print(sum)
    case "-":
        print(sub)
    case "*":
        print(mul)
    case "/":
        print(div)
"""

