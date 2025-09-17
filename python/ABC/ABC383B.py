H, W, D = map(int, input().split())
S = [input() for _ in range(H)]
# print(S)

# 床リストを作成
P = [(i, j) for i in range(H) for j in range(W) if S[i][j] == '.']
# print(P)

# 加湿される床をsetのlistで管理
masks = [0] * len(P)
for i, (x, y) in enumerate(P):
    m = 0
    for j, (u, v) in enumerate(P):
        if abs(x - u) + abs(y - v) <= D:
            m |= 1 << j
    masks[i] = m
# print(masks)

# 2つの加湿器で加湿される床の数を合成してansに格納
ans = []
for i in range(len(masks)):
    for j in range(i + 1, len(masks)):
        ans.append(bin(masks[i] | masks[j]).count('1'))

# 加湿される床の数の最大値を表示
# print(ans)
print(max(ans))

"""
マンハッタン距離に入るマスが“加湿される”。机 # は数えない（そもそも床だけ数える）。
全床マス列挙：床座標を配列 P に集める（最大でも 100 マス）。

前処理（カバレッジのマスク化）
各床マス p を「設置点」としたとき、加湿される床マス集合を ビット集合（整数）にして持つ。
mask[p] の k ビット目が 1 ⇔ P[k] が p から距離 ≤ D。

これで 2 台置くときの被覆は mask[i] | mask[j]、加湿床数は (mask[i] | mask[j]).bit_count() で一発。

masks[i] | masks[j]
2つのビットマスク（= 加湿床集合）を OR して
和集合を作る。

bin( … )
その整数を 2進数文字列に変換する。
例: 13 → '0b1101'

.count("1")
文字列中の "1" の数を数える。
つまり「和集合のビット列に立っているビット数」。
"""
