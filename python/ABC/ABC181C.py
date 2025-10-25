from itertools import combinations
import logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


N = int(input())
XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
logging.debug(f"{XY = }")


def is_collinear(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


for a, b, c in combinations(XY, 3):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    if is_collinear(x1, y1, x2, y2, x3, y3):
        print("Yes")
        exit()
print("No")

"""
数学的な気づき系

3点が一直線上にあるかどうかは、3点で作る三角形の面積が0かどうかで判定できます。

https://atcoder.jp/contests/abc181/tasks/abc181_c
https://chatgpt.com/c/68fc950d-c774-8321-840d-52624b55bc74
"""
