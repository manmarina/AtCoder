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

    if b not in dd[a]:
        continue
    if c not in dd[a]:
        continue
    if a not in dd[b]:
        continue
    if c not in dd[b]:
        continue
    ans.append((a, b, c))

# print(ans)

print(len(ans))
