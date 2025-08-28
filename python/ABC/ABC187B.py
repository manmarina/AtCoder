from itertools import combinations

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

count = 0
for (x1, y1), (x2, y2) in combinations(xy, 2):
    dy = y2 - y1
    dx = x2 - x1
    # if abs(dy / dx) <= 1:
    if abs(dy) <= abs(dx):
        count += 1
print(count)
