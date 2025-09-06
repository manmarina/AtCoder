N, D = map(int, input().split())
T, L = [], []
for _ in range(N):
    t, l = map(int, input().split())
    T.append(t)
    L.append(l)

for k in range(1, D + 1):
    best = 0
    for i in range(N):
        w = T[i] * (L[i] + k)       # = T[i]*L[i] + T[i]*k
        if w > best:
            best = w
    print(best)
