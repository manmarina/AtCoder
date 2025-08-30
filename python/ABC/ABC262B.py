from collections import defaultdict
from itertools import combinations

N, M = map(int, input().split())
UV = [list(map(int, input().split())) for _ in range(M)]

dd = defaultdict(set)
for u, v in UV:
    dd[u].add(v)
    dd[v].add(u)

# print(dd)

ans = []
for a, b, c in combinations(dd.keys(), 3):

    # print((a, b, c))

    # 三角形条件：ab, bc, ca の3本がある
    if (b in dd[a]) and (c in dd[a]) and (c in dd[b]):
        ans.append((a, b, c))

# print(ans)

print(len(ans))
