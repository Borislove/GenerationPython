# Количество членов
"""На вход программе подается последовательность слов,
каждое слово на отдельной строке. Концом последовательности является одно из трех слов:
«стоп», «хватит», «достаточно» (маленькими буквами, без кавычек).
Напишите программу, которая выводит общее количество членов данной последовательности."""

text = ''
counter = -1
while text not in ('стоп', 'хватит', 'достаточно'):
    text = input()
    counter += 1
print(counter)
