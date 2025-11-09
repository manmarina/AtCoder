from itertools import combinations


N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for t1, t2, t3 in combinations(XY, 3):
    x1, y1 = t1
    x2, y2 = t2
    x3, y3 = t3
    # print(t1, t2, t3)
    gaiseki = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    if gaiseki != 0:
        ans += 1

print(ans)

"""
数学的な気づき系
外積を利用して3点が三角形をなすか判定する。

https://atcoder.jp/contests/abc224/tasks/abc224_c
"""
