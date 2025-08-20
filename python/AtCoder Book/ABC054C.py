from itertools import permutations

N, M = map(int, input().split())
# adj = [set() for _ in range(N + 1)]
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    # adj[a].add(b)
    # adj[b].add(a)
    adj[a].append(b)
    adj[b].append(a)

print(adj)

ans = 0
for perm in permutations(range(2, N + 1)):  # 頂点1は固定
    prev = 1
    for v in perm:
        if v not in adj[prev]:
            break
        prev = v
    else:
        ans += 1
        print(perm)

print(ans)
