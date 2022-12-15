def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = int(input())
if is_even(number):
    print('Это число четное. ')
else:
    print('Это число нечетное.')