# v2.0
lst = [int(input()) for _ in range(4)]
print('YES' if (lst[0] + lst[1] + lst[2] + lst[3]) % 2 == 0 else 'NO')

# v2.1
print("YES" if sum(int(input()) for _ in range(4)) % 2 == 0 else "NO")
