# v1.3
num = int(input())
positive_number = (num % 2 == 0)
if num == 0:
    print('зеленый')
elif (1 <= num <= 10) or (19 <= num <= 28):
    print('черный' if positive_number else 'красный')
elif (11 <= num <= 18) or (29 <= num <= 36):
    print('красный' if positive_number else 'черный')
else:
    print('ошибка цвета')
