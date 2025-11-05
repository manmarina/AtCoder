H, W = map(int, input().split())
S = [input() for _ in range(H)]
# print(S)

min_i = 1000
min_j = 1000
max_i = 0
max_j = 0

# 黒いマスの領域を調べる
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            min_i = min(min_i, i)
            min_j = min(min_j, j)
            max_i = max(max_i, i)
            max_j = max(max_j, j)

# print("min_i:", min_i, "min_j:", min_j,)
# print("max_i:", max_i, "max_j:", max_j,)

# 黒いマスの領域内に、白いマスがあったら達成不能
for i in range(min_i, max_i + 1):
    for j in range(min_j, max_j + 1):
        if S[i][j] == '.':  # 白いマスがあったら終了
            print("No")
            exit()

print("Yes")

"""
カーソル系
黒いマスがどの領域にあるかを調べる(領域 Dとする)。
領域 Dの中に、白いマスが1個でもあったら D内で黒い長方形を作ることはできない。

Yuulis
https://yuulis.hatenablog.com/entry/ABC-390-C

https://atcoder.jp/contests/abc390/tasks/abc390_c
"""
