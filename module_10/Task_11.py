# Переворот
s = input()
s1 = s.find('h')
s2 = s.rfind('h')
print(s[:s1 + 1] + s[s2 - 1:s1:-1] + s[s2:])
