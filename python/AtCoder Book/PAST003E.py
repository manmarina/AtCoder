N, M, Q = map(int, input().split())

G = [[] for i in range(N)]

for i in range(M):
    u, v = map(int, input().split())

    u -= 1
    v -= 1

    G[u].append(v)
    G[v].append(u)

# print('G', G)

col = list(map(int, input().split()))

# print()
# print("col", col)

query = []
for i in range(Q):
    t, x, *y = map(int, input().split())

    # print()
    # print('t', t)
    # print('x', x)
    # print('y', y)

    x -= 1

    query.append(col[x])

    if t == 1:
        for v in G[x]:
            col[v] = col[x]
    else:
        col[x] = y[0]

# print()
print(*query, sep='\n')
