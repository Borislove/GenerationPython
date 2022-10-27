# ход коня

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# test up
left_up_1 = (x1 == x2 + 1) and (y1 == y2 + 2)
left_up_2 = (x1 == x2 + 2) and (y1 == y2 + 1)

right_up_1 = (x1 == x2 - 1) and (y1 == y2 + 2)
right_up_2 = (x1 == x2 - 2) and (y1 == y2 + 1)

# test down
right_down_1 = (x1 == x2 - 2) and (y1 == y2 - 1)
right_down_2 = (x1 == x2 - 1) and (y1 == y2 - 2)

left_down_1 = (x1 == x2 + 2) and (y1 == y2 - 1)
left_down_2 = (x1 == x2 + 1) and (y1 == y2 - 2)

if (left_up_1 or left_up_2) or (right_up_1 or right_up_2) or (
        right_down_1 or right_down_2) or (left_down_1 or left_down_2):
    print('ok')
else:
    print('no')

print(y1 == y2 + 2)
