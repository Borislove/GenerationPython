# Манхэттенское расстояние
#

p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())

p = abs(p1 - q1) + abs(p2 - q2)
print(p)

lst = [int(input()) for _ in range(4)]
print(abs(lst[0] - lst[2]) + abs(lst[1] - lst[3]))
