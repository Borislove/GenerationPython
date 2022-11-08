counter = 0
for i in range(99, 102):
    temp = i
    print('temp',temp)
    while temp > 0:
        counter += 1
        temp //= 10
print(counter)


print(9//10)