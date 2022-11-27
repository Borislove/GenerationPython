# Три города
"""
Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
"""

"""
city1, city2, city3 = input(), input(), input()

min_title = min(len(city1), len(city2), len(city3))
max_title = max(len(city1), len(city2), len(city3))

city_len1 = len(city1)
city_len2 = len(city2)

if min_title == city_len1:
    print(city1)
elif min_title == city_len2:
    print(city2)
else:
    print(city3)


if max_title == city_len1:
    print(city1)
elif max_title == city_len2:
    print(city2)
else:
    print(city3)

"""

lst = [input() for _ in range(3)]
print(min(lst, key=len), max(lst, key=len), sep='\n')
