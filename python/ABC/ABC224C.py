import sys

N = int(sys.stdin.readline())
P = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 0
for i in range(N):
    x1, y1 = P[i]
    for j in range(i + 1, N):
        x2, y2 = P[j]
        dx1, dy1 = x2 - x1, y2 - y1
        for k in range(j + 1, N):
            x3, y3 = P[k]
            dx2, dy2 = x3 - x1, y3 - y1
            # 外積（面積の2倍）
            if dx1 * dy2 - dx2 * dy1 != 0:
                ans += 1

print(ans)

"""
幾何 全探索（3重ループ） 数え上げ問題（組合せ探索）
チャッピー

キーアイデア：3点が一直線上かどうか = 外積（面積）が0かどうかで判定（実数の傾きは使わない）
"""
