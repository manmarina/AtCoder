# 9x9 の盤面を読み込み
S = [input().strip() for _ in range(9)]


def in_grid(x, y):
    """盤面内かつ '#' かどうかを判定するヘルパー関数"""
    return 0 <= x < 9 and 0 <= y < 9 and S[x][y] == '#'


squares = set()  # 正方形を頂点4つの集合として保存（重複を消す）

# P1 = (i, j) を全探索
for i in range(9):
    for j in range(9):
        # 辺ベクトル v = (dx, dy) を全探索
        for dx in range(-8, 9):
            for dy in range(-8, 9):
                if dx == 0 and dy == 0:
                    continue  # 長さ0のベクトルはダメ

                # 各頂点を計算
                i2, j2 = i + dx, j + dy             # P2 = P1 + v
                # P3 = P2 + v' （v' = (-dy, dx)）
                i3, j3 = i2 - dy, j2 + dx
                i4, j4 = i3 - dx, j3 - dy           # P4 = P3 - v

                # 4点がすべて盤面内で '#'
                if (in_grid(i, j) and in_grid(i2, j2) and
                        in_grid(i3, j3) and in_grid(i4, j4)):
                    # 正方形を頂点4つの集合（順不同）として保存
                    sq = frozenset([(i, j), (i2, j2), (i3, j3), (i4, j4)])
                    squares.add(sq)

# 集合の大きさが正方形の数
print(len(squares))

"""
全探索 + 数学的気づき系
ベクトルを使用して、正方形を判定してカウントする。

P1 ----v----> P2
 |             |
v'            v'
 |             |
 V             V
P4 ----v----> P3

ベクトル (x, y) を 90° 回転すると
    反時計回り → (-y, x)
    時計回り → (y, -x)
数学でよく出てくる定番です。

P1 = (i, j)
P2 = (i + dx,       j + dy)
P3 = (i + dx - dy,  j + dy + dx)
P4 = (i - dy,       j + dx)

https://atcoder.jp/contests/abc275/tasks/abc275_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691c18a8-dbb4-8320-b545-9d684085a6d6
"""
