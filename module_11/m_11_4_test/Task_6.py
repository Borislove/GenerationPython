# Google search - 2 🌶️🌶️
"""
На вход программе подается натуральное число n, затем n строк,
затем число k — количество поисковых запросов, затем k строк — поисковые запросы.
Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.

Формат входных данных
На вход программе подаются натуральное число n — количество строк, затем сами строки в указанном количестве, затем число k, затем сами поисковые запросы.
"""

lst = []
for _ in range(int(input())):
    lst.append(input())

# запросы
lst_request = []
for i in range(int(input())):
    lst_request.append(input())

lst_input = []
counter = 0
for i in range(len(lst)):
    for j in range(len(lst_request)):
        if lst_request[j].lower() in lst[i].lower():
            counter += 1
            if counter == len(lst_request):
                lst_input.append(lst_request[j])
                counter = 0
print(lst_input)
