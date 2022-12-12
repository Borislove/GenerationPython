# Google search - 1
"""
На вход программе подается натуральное число n, затем n строк,
затем еще одна строка — поисковый запрос. Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
"""

num = int(input())

lst = []
for _ in range(num):
    s = input().lower()
    lst.extend(s)
    for _ in range(len(lst)):
        if s in lst:
            print(*lst, sep='\n')
