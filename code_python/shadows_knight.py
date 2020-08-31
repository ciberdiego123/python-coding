def get_mid_point(a, b):
    r = abs(a - b) // 2
    if r == 0:
        r += 1
    x = min(a, b)
    y = max(a, b)
    print(str(x+r))
    return x + r


def get_next_position(x_rang, y_rang, current_position, dir):
    xi = current_position[0]
    yi = current_position[1]
    if dir == "U":
        new_position = (xi, get_mid_point(y_rang[0], yi))
    elif dir == "UR":
        new_position = (get_mid_point(x_rang[1], xi), get_mid_point(y_rang[0], yi))
    elif dir == "R":
        new_position = (get_mid_point(x_rang[1], xi), yi)
    elif dir == "DR":
        new_position = (get_mid_point(x_rang[1], xi), get_mid_point(y_rang[1], yi))
    elif dir == "D":
        new_position = (xi, get_mid_point(y_rang[1], yi))
    elif dir == "DL":
        new_position = (get_mid_point(x_rang[0], xi), get_mid_point(y_rang[1], yi))
    elif dir == "L":
        new_position = (get_mid_point(x_rang[0], xi), yi)
    elif dir == "UL":
        new_position = (get_mid_point(x_rang[0], xi), get_mid_point(y_rang[0], yi))
    else:
        new_position = (-1, -1)
    return new_position


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

x_rang = (0, w - 1)
y_rang = (0, h - 1)
current_position = (x0, y0)
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if dir == "U":
        x_rang = (cp_x, cp_x)
        y_rang = (y_rang[0], cp_y)
    elif dir == "UR":
        x_rang = (cp_x, x_rang[1])
        y_rang = (y_rang[0], cp_y)
    elif dir == "R":
        x_rang = (cp_x, x_rang[1])
        y_rang = (cp_y, cp_y)
    elif dir == "DR":
        x_rang = (cp_x, x_rang[1])
        y_rang = (cp_y, y_rang[1])
    elif dir == "D":
        x_rang = (cp_x, cp_x)
        y_rang = (cp_y, y_rang[1])
    elif dir == "DL":
        x_rang = (x_rang[0], cp_x)
        y_rang = (cp_y, y_rang[1])
    elif dir == "L":
        x_rang = (x_rang[0], cp_x)
        y_rang = (cp_y, cp_y)
    elif dir == "UL":
        x_rang = (x_rang[0], cp_x)
        y_rang = (y_rang[0], cp_y)
    next_position = get_next_position(x_rang, y_rang, current_position, bomb_dir)
    cp_x = current_position[0]
    cp_y = current_position[1]
    current_position = next_position
    print(str(next_position[0]) + " " + str(next_position[1]))