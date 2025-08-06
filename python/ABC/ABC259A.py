N, M, X, T, D = map(int, input().split())

if X <= M:
    tall = T
else:
    tall = T - D * (X - M)

print(tall)
