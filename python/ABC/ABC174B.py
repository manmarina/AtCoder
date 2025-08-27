N, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

count = 0
for x, y in XY:
    if x**2 + y**2 <= D**2:
        count += 1

print(count)
