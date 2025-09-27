N, L, R = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

count = 0
for x, y in XY:
    if x <= L and y >= R:
        count += 1
print(count)
