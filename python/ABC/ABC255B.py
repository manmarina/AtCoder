from math import hypot

N, K = map(int, input().split())
A = tuple(map(int, input().split()))
A = [a - 1 for a in A]
XY = [tuple(map(int, input().split())) for _ in range(N)]

# print(A)
# print(XY)

ans = []
for x1, y1 in XY:

    # print()
    # print(1, (x1, y1))

    mn = 10**18
    for a in A:
        x2, y2 = XY[a]

        dist = hypot(x1 - x2, y1 - y2)
        mn = min(mn, dist)

        # print(2, (x2, y2))
        # print(dist)
    ans.append(mn)

# print(ans)

print(max(ans))
