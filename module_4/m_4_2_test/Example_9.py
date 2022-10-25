# ------------input--------------------------------------------------------------
num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
# --------------------------------------------------------------------------------

# ---------------------------test column-----------------------------------------
column_position_up = (num1 == num3) and ((num2 - 1) == num4)
column_position_down = (num1 == num3) and ((num2 + 1) == num4)

column_position_left = ((num1 - 1) == num3) and ((num2 == num4))
column_position_right = ((num1 + 1) == num3) and ((num2 == num4))

column_passed = column_position_up \
                or column_position_down \
                or column_position_left \
                or column_position_right

# ---------------------------test diagonal---------------------------------------
vertical_position_up_left = ((num1 - 1) == num3) and ((num2 - 1) == num4)
vertical_position_up_right = ((num1 + 1) == num3) and ((num2 - 1) == num4)

vertical_position_down_left = ((num1 - 1) == num3) and ((num2 + 1) == num4)
vertical_position_down_right = ((num1 + 1) == num3) and ((num2 + 1) == num4)

diagonal_position_passed = (vertical_position_up_left \
                            or vertical_position_up_right \
                            or vertical_position_down_left \
                            or vertical_position_down_right)
# --------------------------------------------------------------------------------
if column_passed or diagonal_position_passed:
    print('YES')
else:
    print('NO')

"""
print('up_left')
print(vertical_position_up_left)

print('up_right')
print(vertical_position_up_right)

print('down_left')
print(vertical_position_down_left)

print('down_right')
print(vertical_position_down_right)
"""
