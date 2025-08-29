from math import hypot

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

# print(xy)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        d = hypot(x1 - x2, y1 - y2)
        if d > ans:
            ans = d
print(ans)
