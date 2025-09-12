from collections import defaultdict
from itertools import permutations


N, M = map(int, input().split())
ab = [list(map(int, input().split()))for _ in range(M)]

G = defaultdict(set)
for a, b in ab:
    G[a].add(b)
    G[b].add(a)
# print(G)

ans = []
for root in permutations(range(2, N + 1)):
    root = [1, *root]
    # print(root)

    for i in range(N - 1):
        r = root[i + 1]
        g = G[root[i]]
        if r not in g:
            break
    else:
        ans.append(root)

# print(ans)
print(len(ans))
