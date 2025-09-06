H, W, D = map(int, input().split())
S = [input().strip() for _ in range(H)]

# 床マス一覧
P = [(i, j) for i in range(H) for j in range(W) if S[i][j] == '.']
F = len(P)

# 各床マスを設置点にしたときの被覆マスク
masks = [0] * F
for i, (x, y) in enumerate(P):
    m = 0
    for k, (u, v) in enumerate(P):
        if abs(x - u) + abs(y - v) <= D:
            m |= 1 << k
    masks[i] = m

print(P)
print(masks)

# 2点選んで最大被覆（popcount を bin().count で代用）
ans = 0
for i in range(F):
    for j in range(i + 1, F):
        ans = max(ans, bin(masks[i] | masks[j]).count("1"))
print(ans)

"""
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
