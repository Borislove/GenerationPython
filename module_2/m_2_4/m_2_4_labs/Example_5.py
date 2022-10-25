a, b = int(input()), int(input())


def double(num):
    return num * num


def cube(num):
    return num * num * num


def sum():
    return a + b


# f(a,b) = 3(a + b)^3 + 275b^2 - 127a - 41
print(3 * (cube(sum())) + 275 * double(b) - 127 * a - 41)
