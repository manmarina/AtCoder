from itertools import permutations

N, M = map(int, input().split())
g = [[False] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a][b] = g[b][a] = True
# print(g) # ex.[[False, True, True], [True, False, True], [True, True, False]]

ans = 0
for perm in permutations(range(1, N)):  # 出発は0(=頂点1)固定
    print(perm)

    ok = True
    cur = 0
    for nxt in perm:
        if not g[cur][nxt]:
            ok = False
            break
        cur = nxt
    if ok:
        ans += 1
print(ans)

"""
順列全探索
グラフを2次元配列で管理
"""
