H, W, X, Y = map(int, input().split())
S = []
for i in range(H):
    S.append(input())


def count_visible(row_count, col_count, x_home, y_home, map):
    x_home -= 1
    y_home -= 1
    directions = ["right", "left", "upper", "lower"]
    count = 1
    for direction in directions:
        if direction == "right":
            gain = 1
            while 1:
                if y_home + gain > col_count - 1:
                    break
                if map[x_home][y_home + count] == '#':
                    break
                count += 1
                gain += 1
        elif direction == "left":
            gain = 1
            while 1:
                if y_home - gain < 0:
                    break
                if map[x_home][y_home - gain] == '#':
                    break
                count += 1
                gain += 1
        elif direction == "upper":
            gain = 1
            while 1:
                if x_home - gain < 0:
                    break
                if map[x_home - gain][y_home] == '#':
                    break
                count += 1
                gain += 1
        elif direction == "lower":
            gain = 1
            while 1:
                if x_home + gain > row_count - 1:
                    break
                if map[x_home + gain][y_home] == '#':
                    break
                count += 1
                gain += 1
    return count


print(count_visible(H, W, X, Y, S))
