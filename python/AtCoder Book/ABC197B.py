H, W, X, Y = map(int, input().split())
S = []
for i in range(H):
    S.append(input())


def count_visible_1way(row_count, col_count, x_home, y_home, map, direction):
    if direction == "right":
        condition_1 = "y_home + gain > col_count - 1"
        condition_2 = "map[x_home][y_home + gain]"
    elif direction == "left":
        condition_1 = "y_home - gain < 0"
        condition_2 = "map[x_home][y_home - gain]"
    elif direction == "upper":
        condition_1 = "x_home - gain < 0"
        condition_2 = "map[x_home - gain][y_home]"
    elif direction == "lower":
        condition_1 = "x_home + gain > row_count - 1"
        condition_2 = "map[x_home + gain][y_home]"
    gain = 1
    while 1:
        if eval(condition_1):
            break
        if eval(condition_2) == '#':
            break
        gain += 1
    return gain - 1


def count_visible(row_count, col_count, x_home, y_home, map):
    x_home -= 1
    y_home -= 1
    directions = ["right", "left", "upper", "lower"]
    count = 1
    for direction in directions:
        count += count_visible_1way(row_count,
                                    col_count,
                                    x_home,
                                    y_home,
                                    map,
                                    direction)
    return count


print(count_visible(H, W, X, Y, S))
