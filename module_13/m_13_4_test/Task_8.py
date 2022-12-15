# Merge lists 1

# объявление функции
def merge(list1, list2):
    lst = []
    lst.extend(list1)
    lst.extend(list2)
    return sorted(lst)


# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))
