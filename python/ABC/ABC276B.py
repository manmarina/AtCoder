N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
# print(AB)

adj = [[] for _ in range(N + 1)]
for a, b in AB:
    adj[a].append(b)
    adj[b].append(a)
# print(adj)

for i in range(1, N + 1):
    print(len(adj[i]), *sorted(adj[i]))
