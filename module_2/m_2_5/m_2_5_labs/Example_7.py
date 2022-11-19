# Мандарины

"""
n школьников делят k мандаринов поровну,
неделящийся остаток остается в корзине. Сколько целых мандаринов достанется каждому школьнику?
 Сколько целых мандаринов останется в корзине?"""

"""
student = int(input())
fruit = int(input())

print(fruit // student)
print(fruit%student)
"""

# v2
student, fruit = int(input()), int(input())
print(fruit // student, fruit % student, sep='\n')
