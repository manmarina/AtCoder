from itertools import permutations

# グラフを隣接行列で管理する
N, M = map(int, input().split())
G = [[False] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1  # 0-index
    G[a][b] = G[b][a] = True

# 順列を全部試す（先頭が0以外になったら打ち切り）
res = 0
for ord in permutations(range(N)):
    if ord[0] != 0:
        break
    ok = True
    for i in range(N - 1):
        if not G[ord[i]][ord[i + 1]]:
            ok = False
            break
    if ok:
        res += 1

print(res)

"""
順列全探索
グラフを2次元配列で管理
"""
