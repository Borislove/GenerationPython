# Ход ферзя
num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
x1, y1, x2, y2 = num1, num2, num3, num4

column_position_up = (x1 == x2) and (y1 > y2)
column_position_down = (x1 == x2) and (y1 < y2)

column_position_left = (x1 > x2) and (y1 == y2)
column_position_right = (x1 < x2) and (y1 == y2)

column_position_passed = column_position_up or column_position_down or column_position_left or column_position_right
# ---------------------------test diagonal---------------------------------------
vertical_left_up = (x2 < x1) and (y2 < y1)
vertical_right_up = (x2 > x1) and (y2 < y1)
vertical_left_down = (x2 < x1) and (y2 > y1)
vertical_right_down = (x2 > x1) and (y2 > y1)

diagonal_position_passed = (vertical_left_up \
                            or vertical_right_up \
                            or vertical_left_down \
                            or vertical_right_down)

outside_left = (x1 > x2 + 3) and (y2 < y1)
test = (x1 - x2) != (y1 - y2)
test_2 = (x1 + x2) != (y1 - y2)

if (diagonal_position_passed or column_position_passed) or test or test_2:
    print('YES')
else:
    print('NO')

print(outside_left)
