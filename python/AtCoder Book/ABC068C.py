N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

print(G)

start = 0
goal = N - 1
for g in G:
    if start in g and goal in g:
        print("POSSIBLE")
        break
else:
    print("IMPOSSIBLE")
