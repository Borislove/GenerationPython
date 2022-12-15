# Количество дней
# объявление функции
def get_days(month):
    if month == 6 or month == 9 or month == 4 or month == 11:
        return 30
    elif month == 2:
        return 28
    else:
        return 31


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
