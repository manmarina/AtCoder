N, M = map(int, input().split())

INF = 10**9
X = 0
for i in range(M + 1):
    X += N**i
    if X > INF:
        print("inf")
        break
else:
    print(X)
