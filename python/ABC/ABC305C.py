H, W = map(int, input().split())
S = [input() for _ in range(H)]
# print(S)

# 探索範囲を確定する
min_i, min_j = 500, 500
max_i, max_j = 0, 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            min_i = min(min_i, i)
            min_j = min(min_j, j)
            max_i = max(max_i, i)
            max_j = max(max_j, j)

# print("min_i:", min_i, "min_j:", min_j)
# print("max_i:", max_i, "max_j:", max_j)

# 探索範囲内の'.'を探す。
for i in range(min_i, max_i + 1):
    for j in range(min_j, max_j + 1):
        if S[i][j] == '.':
            print(i + 1, j + 1)

"""
カーソル系
探索範囲を確定->探索範囲内の'.'を探す。

けんちょんの解説
https://atcoder.jp/contests/abc305/tasks/abc305_c

https://atcoder.jp/contests/abc305/tasks/abc305_c
"""
