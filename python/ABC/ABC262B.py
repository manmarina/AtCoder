N, M = map(int, input().split())
adj = [[False] * N for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u][v] = adj[v][u] = True

print(adj)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if not adj[i][j]:
            continue
        for k in range(j + 1, N):
            if adj[i][k] and adj[j][k]:
                ans += 1

print(ans)
