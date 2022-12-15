# Найти всех

# объявление функции
def find_all(target, symbol):
    lst = []
    for i in range(len(target)):
        if symbol in target:
            lst.append([symbol])
        return lst


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
