birds = 5000  # глобальная переменная


def print_texas():
    birds = 1000  # локальная переменная
    print('В Техасе обитает', birds, 'птиц.')


def print_california():
    birds = 7000  # локальная переменная
    print('В Калифорнии обитает', birds, 'птиц.')


print_texas()
print_california()