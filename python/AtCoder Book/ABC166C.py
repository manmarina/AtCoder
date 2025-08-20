N, M = map(int, input().split())
H = list(map(int, input().split()))
H.insert(0, 0)

G = [[] for i in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)
# print(G)

good = 0
for i in range(1, len(G)):
    if len(G[i]) == 0:
        good += 1
    else:
        for v in G[i]:
            if H[i] <= H[v]:
                break
        else:
            good += 1

print(good)
