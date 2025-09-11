import sys
from itertools import permutations

input = sys.stdin.readline
N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for order in permutations(range(1, N)):  # 都市0を出発固定、残りを並べる
    t = 0
    cur = 0
    # 0 -> order[0] -> ... -> order[-1] -> 0
    for nxt in order:
        t += T[cur][nxt]
        if t > K:  # 任意の枝刈り（無くてもAC）
            break
        cur = nxt
    else:
        t += T[cur][0]
        if t == K:
            ans += 1

print(ans)
