# Метод extend()
"""
Можно также расширить список другим списком, путем вызова метода extend().

"""

numbers = [0, 2, 4, 6, 8, 10]
odds = [1, 3, 5, 7]

numbers.extend(odds)
print(numbers)
