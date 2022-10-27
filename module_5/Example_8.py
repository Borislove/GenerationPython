x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())


column_position_up = (x1 == x2) and (y1 > y2)
column_position_down = (x1 == x2) and (y1 < y2)

column_position_left = (x1 > x2) and (y1 == y2)
column_position_right = (x1 < x2) and (y1 == y2)

column_posititon_passed = column_position_up or column_position_down or column_position_left or column_position_right

if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2) or column_posititon_passed:
    print('YES')
else:
    print('NO')
