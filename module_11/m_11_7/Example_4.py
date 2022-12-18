"""
n = int(input())
lines = [input() for _ in range(n)]
"""

lines = [input() for _ in range(int(input()))]

numbers = [int(input()) for _ in range(int(input()))]

# список четных чисел от 0 до 20
evens = [i for i in range(21) if i % 2 == 0]  # лучше использовать функцию range(0, 21, 2)
