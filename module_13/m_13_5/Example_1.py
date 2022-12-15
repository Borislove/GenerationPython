number = int(input())
if number % 2 == 0:
    print('Это число четное. ')
else:
    print('Это число нечетное.')


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
