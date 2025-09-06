from math import hypot
N = int(input())
XY = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)] + [(0, 0)]
# print(XY)

ans = 0
for (x1, y1), (x2, y2) in zip(XY, XY[1:]):
    # print((x1, y1), (x2, y2))
    ans += hypot(x1 - x2, y1 - y2)
print(ans)
