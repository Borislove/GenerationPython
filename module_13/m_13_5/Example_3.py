def is_invalid(model):
    if model != 100 and model != 200 and model != 300:
        return True
    else:
        return False


while is_invalid(model):
    print('Допустимыми номерами моделей являются 100, 200 и 300.')
    model = int(input())
