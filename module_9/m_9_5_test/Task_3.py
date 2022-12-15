# Шифр Цезаря 🌶️

num = int(input())
s = input()

for c in s:
    if ord(c) - num < 97:
        print(chr(ord(c) - num + 26), end='')
    else:
        print(chr(ord(c) - num), end='')
