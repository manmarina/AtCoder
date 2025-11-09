N = int(input())
TXY = [list(map(int, input().split())) for _ in range(N)]

cur = (0, 0, 0)
for t2, x2, y2 in TXY:
    t1, x1, y1 = cur
    dd = abs(x1 - x2) + abs(y1 - y2)  # マンハッタン距離
    dt = t2 - t1  # 移動時間
    if dd > dt:  # 距離が移動時間よりも長い時
        print("No")
        exit()
    if dd % 2 != dt % 2:  # 距離と移動時間の偶奇が一致しない時
        print("No")
        exit()
    cur = (t2, x2, y2)

print("Yes")

"""
カーソル系
マンハッタン距離と偶奇を考える。

https://atcoder.jp/contests/abc086/tasks/arc089_a
"""
