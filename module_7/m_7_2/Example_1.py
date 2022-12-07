for i in range(56, 171, 2):
    print(i)

# менее эффективный
for i in range(56, 171):
    if i % 2 == 0:
        print(i)
